
# INTELLIGENT CPU SCHEDULER SIMULATOR

## Project Report

**Project Title:** Intelligent CPU Scheduler Simulator

**Course:** CSE316

**Project Type:** Individual Project

**Interface:** Streamlit Web Dashboard

**Programming Language:** Python

**Algorithms Implemented:**
1. First Come First Serve (FCFS)
2. Shortest Job First (SJF) – Non-preemptive
3. Priority Scheduling – Non-preemptive
4. Round Robin (RR)

---

# 1. Introduction

CPU scheduling is an important function of an operating system. It determines which process gets access to the CPU and for how long.

Different scheduling algorithms use different approaches to select processes. These approaches affect waiting time, turnaround time, response time and CPU utilization.

The Intelligent CPU Scheduler Simulator is a Python-based web application developed using Streamlit. It allows users to enter process details, execute four CPU scheduling algorithms, compare their performance and visualize their execution through Gantt charts.



# 2. Problem Statement

In an operating system, multiple processes compete for CPU execution. Selecting an appropriate scheduling algorithm is important because it directly affects system performance.

Understanding and comparing scheduling algorithms manually can be difficult, especially when processes have different arrival times, burst times and priorities.

The objective of this project is to develop an interactive CPU Scheduling Simulator that implements four scheduling algorithms and provides a visual comparison of their performance.

# 3. Project Objectives

The main objectives of this project are:

1. Implement FCFS, non-preemptive SJF, non-preemptive Priority and Round Robin scheduling algorithms.
2. Allow users to enter process IDs, arrival times, burst times and priorities.
3. Allow users to configure the Round Robin time quantum.
4. Generate Gantt charts to visualize process execution.
5. Calculate average waiting time, average turnaround time and average response time.
6. Calculate CPU utilization and throughput.
7. Compare the performance of all four scheduling algorithms.
8. Provide downloadable CSV reports containing comparison and detailed process results.

# 4. Project Scope

The simulator focuses on CPU scheduling and performance comparison.

It provides:
- Interactive process configuration.
- Four CPU scheduling algorithms.
- Non-preemptive SJF and Priority scheduling.
- Configurable Round Robin time quantum.
- Gantt chart visualization, including CPU idle periods.
- Performance metrics and comparison.
- CSV report downloads.


# 5. Methodology

The project follows a structured development approach:

### Step 1: Input Collection

The user enters the following process information through the Streamlit sidebar:

- Process ID
- Arrival Time
- Burst Time
- Priority
- Time Quantum (for Round Robin)

### Step 2: Process Scheduling

The entered processes are passed to the four scheduling algorithms. Each algorithm determines the execution order based on its scheduling rules.

### Step 3: Performance Calculation

After scheduling, the simulator calculates:

- Waiting Time
- Turnaround Time
- Response Time
- CPU Utilization
- Throughput

### Step 4: Visualization

The application generates Gantt charts to represent process execution and CPU idle periods.

### Step 5: Performance Comparison

A comparison table and performance analysis section help users evaluate the results of all four algorithms.

### Step 6: Report Generation

Users can download two CSV files:
- CPU Scheduling Comparison Report
- CPU Scheduling Detailed Results

# 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| Pandas | Process data and result tables |
| Matplotlib | Gantt charts and performance graphs |
| VS Code | Development environment |
| Git | Version control |


# 7. Scheduling Algorithms

## 7.1 First Come First Serve (FCFS)

FCFS is a non-preemptive scheduling algorithm in which processes are executed in the order of their arrival time.

**Working Principle:**
1. Processes are arranged according to arrival time.
2. The CPU selects the process that arrived first.
3. Once execution begins, the process runs until completion.
4. The next available process is selected.

**Key Characteristic:** Simple and fair according to arrival order, but may cause long waiting times.

## 7.2 Shortest Job First (SJF) – Non-preemptive

SJF selects the available process with the shortest burst time.

**Working Principle:**
1. Check which processes have arrived.
2. Select the available process with the smallest burst time.
3. Execute it until completion.
4. Repeat until all processes finish.

**Key Characteristic:** Can reduce average waiting time, but longer processes may experience starvation.

## 7.3 Priority Scheduling – Non-preemptive

Priority Scheduling selects the available process with the highest priority.

In this project, a smaller priority number represents a higher priority.

**Working Principle:**
1. Check the available processes.
2. Select the process with the highest priority.
3. Execute it until completion.
4. Repeat until all processes finish.

**Key Characteristic:** Important processes can execute earlier, but low-priority processes may experience starvation.

## 7.4 Round Robin (RR)

Round Robin is a preemptive scheduling algorithm that gives each process a fixed CPU time called the time quantum.

**Working Principle:**
1. Processes enter a ready queue according to arrival time.
2. The CPU selects the first process in the queue.
3. The process executes for the time quantum or until completion.
4. If unfinished, it returns to the end of the ready queue.
5. The process continues receiving CPU time until completion.

**Key Characteristic:** Provides fair CPU sharing and is commonly associated with time-sharing systems.


# 8. Performance Metrics and Formulas

The simulator evaluates scheduling algorithms using five performance metrics.

## 8.1 Waiting Time

Waiting Time is the total time a process spends waiting in the ready queue.

**Formula:**

Waiting Time = Turnaround Time - Burst Time

## 8.2 Turnaround Time

Turnaround Time is the total time taken by a process from its arrival until its completion.

**Formula:**

Turnaround Time = Completion Time - Arrival Time

## 8.3 Response Time

Response Time is the time between process arrival and its first CPU execution.

**Formula:**

Response Time = First Start Time - Arrival Time

## 8.4 Average Waiting Time

It represents the average waiting time of all processes.

**Formula:**

Average Waiting Time = Sum of Waiting Times / Number of Processes

## 8.5 Average Turnaround Time

It represents the average turnaround time of all processes.

**Formula:**

Average Turnaround Time = Sum of Turnaround Times / Number of Processes

## 8.6 CPU Utilization

CPU Utilization represents the percentage of elapsed time during which the CPU is busy.

**Formula:**

CPU Utilization = (Total Burst Time / Total Elapsed Time) × 100

## 8.7 Throughput

Throughput represents the number of processes completed per unit of elapsed time.

**Formula:**

Throughput = Number of Completed Processes / Total Elapsed Time

# 9. Expected Output

The simulator produces:

1. A process input table.
2. A scheduling comparison table.
3. Four Gantt charts.
4. Performance analysis identifying the best algorithm for waiting time, turnaround time and response time.
5. Downloadable CSV reports.


# 10. System Architecture

The CPU Scheduling Simulator follows a modular architecture consisting of three main layers.

### 10.1 User Interface Layer

The Streamlit application provides:
- Process input fields.
- Process table.
- Algorithm comparison button.
- Performance comparison dashboard.
- Gantt chart visualizations.
- CSV download options.

### 10.2 Scheduling Logic Layer

The `algorithms.py` module contains the implementation of:
- FCFS
- Non-preemptive SJF
- Non-preemptive Priority
- Round Robin

Each algorithm processes the input data and calculates individual process metrics.

### 10.3 Data Processing and Visualization Layer

Pandas is used to organize process results and generate comparison tables.

Matplotlib generates Gantt charts and performance graphs.

### 10.4 Application Workflow

1. User enters process details.
2. Input data is stored in Streamlit session state.
3. User clicks Compare All Algorithms.
4. All four scheduling algorithms execute.
5. Performance metrics are calculated.
6. Results are displayed in tables and charts.
7. Users can download CSV reports.

# 11. Project File Structure

The project is organized as follows:

CPU_Scheduler_Simulator/
│
├── venv/
│
├── app.py
│
├── algorithms.py
│
├── requirements.txt
│
└── Project_Documentation/
    └── Project_Report.md


# 11. Testing and Validation

The simulator is tested using different process configurations to verify the scheduling algorithms and performance calculations.

## 11.1 Functional Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Add a valid process | Process is added successfully |
| TC02 | Add duplicate Process ID | Error message is displayed |
| TC03 | Add an empty Process ID | Validation error is displayed |
| TC04 | Execute FCFS | Processes execute in arrival order |
| TC05 | Execute SJF | Shortest available process executes first |
| TC06 | Execute Priority | Highest-priority available process executes first |
| TC07 | Execute Round Robin | Processes execute using the configured time quantum |
| TC08 | Delayed process arrival | CPU idle periods are represented |
| TC09 | Compare algorithms | Performance comparison is displayed |
| TC10 | Download CSV reports | CSV files are generated successfully |

## 11.2 Validation

The project was tested with multiple process configurations, including:

- Processes with different arrival times.
- Processes with different burst times.
- Processes with different priorities.
- Different Round Robin time quantum values.
- Processes arriving after periods of CPU inactivity.

The test cases help verify the scheduling logic, visualizations and report generation features.

# 12. Limitations

The current version of the simulator has the following limitations:

1. SJF and Priority Scheduling are implemented in non-preemptive forms only.
2. Round Robin uses a user-configurable time quantum.
3. The simulator focuses on CPU scheduling and does not model memory management or I/O scheduling.
4. Results depend on the process information entered by the user.


# 13. Conclusion

The Intelligent CPU Scheduler Simulator provides an interactive platform for understanding and comparing different CPU scheduling algorithms.

The project successfully brings together FCFS, non-preemptive SJF, non-preemptive Priority Scheduling and Round Robin in a single Streamlit-based application.

Through Gantt charts, performance metrics, comparison tables and downloadable reports, users can observe how different scheduling strategies affect CPU performance.

This project also provides practical experience in Python programming, algorithm implementation, data processing and visualization.

# 14. Future Enhancements

The project can be extended with the following features:

1. Preemptive SJF (Shortest Remaining Time First).
2. Preemptive Priority Scheduling.
3. Improved Gantt chart customization.
4. Interactive process editing.
5. Additional performance metrics.
6. Exporting reports in PDF format.

# 15. References

1. Operating System Concepts – Abraham Silberschatz, Peter B. Galvin and Greg Gagne.
2. Python Documentation: https://docs.python.org/3/
3. Streamlit Documentation: https://docs.streamlit.io/
4. Pandas Documentation: https://pandas.pydata.org/docs/
5. Matplotlib Documentation: https://matplotlib.org/stable/

## 16. Project Screenshots

### 16.1 Process Table
![Process Table](Screenshots/01_Process_table.png)

### 16.2 Algorithm Comparison
![Algorithm Comparison](Screenshots/02_Algorithm_Comparison.png)

### 16.3 Gantt Charts
![Gantt Charts](Screenshots/03_Gantt_Charts.png)
![Gantt Charts](Screenshots/03_Gantt_Charts2.png)

### 16.4 Performance Analysis
![Performance Analysis](Screenshots/04_Performance_Analysis.png)
![Performance Analysis](Screenshots/04_Performance_Analysis2.png)


**End of Project Report**

