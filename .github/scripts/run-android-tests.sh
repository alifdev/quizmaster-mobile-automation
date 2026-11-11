
#!/usr/bin/env bash

set -euo pipefail

echo "Installing QuizMaster APK..."
adb install -r app-release.apk

echo "Starting Appium server..."
nohup appium --address 127.0.0.1 --port 4723 > appium.log 2>&1 &

echo "Waiting for Appium server..."

for attempt in $(seq 1 30); do
    if curl -fsS http://127.0.0.1:4723/status > /dev/null; then
        echo "Appium server is ready."
        break
    fi

    sleep 2
done

if ! curl -fsS http://127.0.0.1:4723/status > /dev/null; then
    echo "Appium server failed to start."
    cat appium.log
    exit 1
fi

echo "Running Android automation tests..."

pytest -v \
    --html=reports/pytest-report.html \
    --self-contained-html \
    --junitxml=reports/junit-results.xml
