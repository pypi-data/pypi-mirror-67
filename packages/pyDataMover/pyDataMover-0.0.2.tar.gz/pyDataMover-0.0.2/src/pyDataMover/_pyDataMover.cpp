#include <_pyDataMover.hpp>

#include <aws/core/Aws.h>
#include <aws/core/utils/memory/stl/AWSString.h>
#include <aws/core/utils/logging/DefaultLogSystem.h>
#include <aws/core/utils/logging/ConsoleLogSystem.h>
#include <aws/core/utils/logging/AWSLogging.h>
#include <aws/common/logging.h>


std::mutex abortMutex;
std::condition_variable abortCondVar;
bool isAbortCancelled = false;

std::shared_ptr<dm::WdtAbortChecker> setupAbortChecker() {
    int abortSeconds = 30;
    if (abortSeconds <= 0) {
        return nullptr;
    }
    DMLOG(1) << "Setting up abort " << abortSeconds << " seconds.";
    static std::atomic<bool> abortTrigger{false};
    auto res = std::make_shared<dm::WdtAbortChecker>(abortTrigger);
    auto lambda = [=] {
        DMLOG(1) << "Will abort in " << abortSeconds << " seconds.";
        std::unique_lock<std::mutex> lk(abortMutex);
        bool isNotAbort =
            abortCondVar.wait_for(lk, std::chrono::seconds(abortSeconds),
                              [&]() -> bool { return isAbortCancelled; });
        if (isNotAbort) {
            DMLOG(1) << "Already finished normally, no abort.";
        } else {
            DMLOG(1) << "Requesting abort.";
            abortTrigger.store(true);
        }
    };
    // Run this in a separate thread concurrently with sender/receiver
    static auto f = std::async(std::launch::async, lambda);
    return res;
}

void cancelAbort() {
    {
        std::unique_lock<std::mutex> lk(abortMutex);
        isAbortCancelled = true;
        abortCondVar.notify_one();
    }
    std::this_thread::yield();
}

void awsInit(bool debug=false) {
    Aws::SDKOptions awsOptions;
    if(debug){
        awsOptions.loggingOptions.logLevel = Aws::Utils::Logging::LogLevel::Debug;
        awsOptions.loggingOptions.logger_create_fn = [] {
            return std::make_shared<Aws::Utils::Logging::ConsoleLogSystem>(
                Aws::Utils::Logging::LogLevel::Trace);
      };
  }
  Aws::InitAPI(awsOptions);
}

void awsShutdown() {
}
