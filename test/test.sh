#!/bin/bash

echo "Waiting for services to start..."
sleep 10  # Adjust this sleep duration based on your application's startup time

echo "Running backend tests..."
pytest ../Backend/test_app.py

echo "Running frontend tests..."
cd ../Frontend
streamlit run streamlit_app.py --server.headless true --server.enableCORS false --server.port 8501 &
frontend_pid=$!

sleep 5

if ! pgrep -f streamlit; then
  echo "Streamlit app failed to start"
  exit 1
fi


if docker ps | grep -q 19661974/backend; then
  echo "Backend container is running"
else
  echo "Backend container is not running"
fi

if docker ps | grep -q 19661974/frontend; then
  echo "Frontend container is running"
else
  echo "Frontend container is not running"
fi

echo "Killing frontend process..."
kill $frontend_pid

if pgrep -f streamlit; then
  echo "Failed to kill the frontend process"
  exit 1
fi

echo "Tests completed."

