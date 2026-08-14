# Pool Controller

> 🚧 This project is under active development.

A modular monitoring and control system for residential swimming pool pumps.

The project is being developed incrementally, starting with a simple software MVP and gradually moving toward real hardware integration.

---

## Current MVP

The current version provides basic motor control through a web dashboard.

Current capabilities:

- Turn the motor ON
- Turn the motor OFF
- Display the current motor status
- Control the motor through a FastAPI web interface
- Separate hardware, control logic, and API layers

---

## Architecture

Dashboard → FastAPI → MotorController → Virtual Motor

The current motor is a software simulation.

The architecture is designed so that the virtual motor can later be replaced by real hardware such as a relay/contactor and MCU.

---

## Project Structure

Pool-Controller/

src/
- api/api_server.py
- controller/motor_controller.py
- hardware/motor.py
- main.py

tests/

README.md
requirements.txt
.gitignore

---

## Technologies

- Python
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript

---

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run the API server:

uvicorn src.api.api_server:app --reload

Dashboard:

http://127.0.0.1:8000/dashboard

API documentation:

http://127.0.0.1:8000/docs

---

## API

Turn Motor ON:

POST /motor/on

Turn Motor OFF:

POST /motor/off

Get Motor Status:

GET /motor/status

Example response:

{
    "running": true
}

---

## Roadmap

### MVP 0.1

- [x] Project structure
- [x] Virtual motor
- [x] Motor controller
- [x] FastAPI API
- [x] Web dashboard
- [x] Motor ON/OFF control
- [x] Motor status display

### MVP 0.2

- [ ] Automatic status monitoring
- [ ] Real motor feedback
- [ ] Runtime measurement

### MVP 0.3

- [ ] Current measurement
- [ ] Current history
- [ ] Basic abnormal-current detection

### Future

- [ ] Real MCU hardware
- [ ] Relay/contactor control
- [ ] MQTT communication
- [ ] Remote monitoring
- [ ] Alarm and notification system
- [ ] Historical data
- [ ] Multi-equipment support

---

## Development Philosophy

The project is developed as a sequence of small, testable milestones.

Each milestone should provide a working feature before the next feature is added.

The long-term goal is to transform the prototype into a practical and commercially viable monitoring and control system for residential swimming pools.

---

## Author

Hadi Norouzi

GitHub:

https://github.com/Zaptrons
