# my life: Finite-state machine
This is a Python script that simulates the daily life of a person named Denis using a finite-state machine. The script defines different states representing various activities that Denis can engage in throughout the day. Each state is associated with a specific time of the day and certain conditions for transitioning to other states.

### States
The following states are defined as part of the States enum:

- **sleeping**: Represents the state when Denis is sleeping.
- **running**: Represents the state when Denis is running.
- **eating**: Represents the state when Denis is eating.
- **studying**: Represents the state when Denis is studying.
- **walking**: Represents the state when Denis is walking.
- **working**: Represents the state when Denis is working.
- **training**: Represents the state when Denis is training.
- **chilling**: Represents the state when Denis is chilling.

### Denis Class
The Denis class represents the finite-state machine for simulating Denis's daily life. It has the following methods:

- **__init__()**: Initializes the Denis object and sets the initial state to sleeping_state.
- **_sleeping_state()**: Generator function representing the sleeping state. It determines the next state based on the time of the day and weather conditions.
- **_running_state()**: Generator function representing the running state. It transitions to the eating state at a specific time.
- **_eating_state()**: Generator function representing the eating state. It transitions to the studying state at a specific time.
- **_working_state()**: Generator function representing the working state. It transitions to the walking state or chilling state based on certain conditions at a specific time.
- **_studying_state()**: Generator function representing the studying state. It transitions to the training state or working state at specific times based on certain conditions.
- **_walking_state()**: Generator function representing the walking state. It transitions to the sleeping state at a specific time.
- **_training_state()**: Generator function representing the training state. It transitions to the working state at a specific time.
- **_chilling_state()**: Generator function representing the chilling state. It transitions to the sleeping state at a specific time.
- **change_poliarity()**: Method to change the polarity of Denis's mood.
- **get_weather()**: Method to determine if it's raining based on a random probability.
- **send(hour)**: Method to send the current hour to the current state for processing.

### live_day() Function
The **live_day()** function simulates a full day in Denis's life. It creates an instance of the Denis class and sends each hour of the day to the Denis object to trigger state transitions and actions.

To run the script and simulate Denis's daily life, simply execute the **live_day()** function.

**Note:** The script is written in Python 3.
