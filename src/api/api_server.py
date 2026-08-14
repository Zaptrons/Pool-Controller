"""
FastAPI API Server

Provides HTTP endpoints for controlling and monitoring
the pool motor.
"""

from fastapi import FastAPI

from src.controller.motor_controller import MotorController
from src.hardware.motor import Motor
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pool Controller")


# Hardware
motor = Motor()

# Business Logic
motor_controller = MotorController(motor)


@app.get("/")
def home():
    return {
        "project": "Pool Controller",
        "status": "Running"
    }


@app.post("/motor/on")
def motor_on():
    motor_controller.start()

    return {
        "motor": "ON"
    }


@app.post("/motor/off")
def motor_off():
    motor_controller.stop()

    return {
        "motor": "OFF"
    }


@app.get("/motor/status")
def motor_status():
    return motor_controller.status()


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Pool Controller</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f4f7;
                text-align: center;
                padding-top: 80px;
            }

            .card {
                background: white;
                width: 350px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }

            h1 {
                margin-bottom: 30px;
            }

            #status {
                font-size: 28px;
                font-weight: bold;
                margin: 30px;
            }

            button {
                padding: 12px 25px;
                margin: 8px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
            }

            .on {
                background: #2ecc71;
                color: white;
            }

            .off {
                background: #e74c3c;
                color: white;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Pool Controller</h1>

            <div>
                Motor Status:
            </div>

            <div id="status">
                Loading...
            </div>

            <button class="on" onclick="turnMotorOn()">
                TURN ON
            </button>

            <button class="off" onclick="turnMotorOff()">
                TURN OFF
            </button>

        </div>


        <script>

            async function updateStatus() {

                const response =
                    await fetch("/motor/status");

                const data =
                    await response.json();

                const status =
                    document.getElementById("status");

                if (data.running) {

                    status.textContent = "🟢 RUNNING";

                } else {

                    status.textContent = "🔴 STOPPED";

                }
            }


            async function turnMotorOn() {

                await fetch(
                    "/motor/on",
                    {
                        method: "POST"
                    }
                );

                await updateStatus();
            }


            async function turnMotorOff() {

                await fetch(
                    "/motor/off",
                    {
                        method: "POST"
                    }
                );

                await updateStatus();
            }


            updateStatus();

        </script>

    </body>

    </html>
    """