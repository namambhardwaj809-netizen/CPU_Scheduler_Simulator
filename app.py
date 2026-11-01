
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from algorithms import (
    fcfs,
    sjf,
    priority_scheduling,
    round_robin
)

st.set_page_config(
    page_title="CPU Scheduling Simulator",
    page_icon="💻",
    layout="wide"
)

st.title("💻 CPU Scheduling Simulator")
st.caption("Compare four CPU scheduling algorithms.")

# Initialize process storage
if "processes" not in st.session_state:
    st.session_state.processes = []

# Sidebar
st.sidebar.header("Process Configuration")

pid = st.sidebar.text_input("Process ID", value="P1")
arrival = st.sidebar.number_input(
    "Arrival Time", min_value=0, value=0
)
burst = st.sidebar.number_input(
    "Burst Time", min_value=1, value=1
)
priority = st.sidebar.number_input(
    "Priority", min_value=1, value=1
)

quantum = st.sidebar.number_input(
    "Time Quantum",
    min_value=1,
    value=2
)

if st.sidebar.button("Add Process"):
    pid = pid.strip()

    if not pid:
        st.sidebar.error("Enter a Process ID.")
    elif any(p["pid"] == pid for p in st.session_state.processes):
        st.sidebar.error("Process ID already exists!")
    else:
        st.session_state.processes.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority
        })
        st.sidebar.success(f"{pid} added!")

# Main process table
st.subheader("📋 Process Table")

if st.session_state.processes:
    df = pd.DataFrame(st.session_state.processes)
    st.dataframe(df, use_container_width=True)

    if st.button("Clear All Processes"):
        st.session_state.processes = []
        st.rerun()
else:
    st.info("Add processes using the sidebar.")

# Run all algorithms
if st.button("Compare All Algorithms", type="primary"):

    if not st.session_state.processes:
        st.warning("Please add at least one process.")

    else:
        processes = st.session_state.processes

        results = {
            "FCFS": fcfs(processes),
            "SJF": sjf(processes),
            "Priority": priority_scheduling(processes)
        }

        rr_results, rr_gantt = round_robin(
            processes, quantum
        )

        results["Round Robin"] = rr_results

        st.session_state.results = results
        st.session_state.rr_gantt = rr_gantt

# Display comparison
if "results" in st.session_state:

    st.divider()
    st.header("📊 Algorithm Comparison")

    comparison = []

    for name, result in st.session_state.results.items():

        avg_waiting = sum(
            p["waiting"] for p in result
        ) / len(result)

        avg_turnaround = sum(
            p["turnaround"] for p in result
        ) / len(result)

        avg_response = sum(
            p["response"] for p in result
        ) / len(result)

        total_burst = sum(
            p["burst"] for p in result
        )

        first_arrival = min(
            p["arrival"] for p in result
        )

        last_completion = max(
            p["completion"] for p in result
        )

        elapsed = last_completion - first_arrival

        cpu_utilization = (
            total_burst / elapsed * 100
            if elapsed > 0 else 0
        )

        throughput = (
            len(result) / elapsed
            if elapsed > 0 else 0
        )

        comparison.append({
            "Algorithm": name,
            "Avg Waiting Time": round(avg_waiting, 2),
            "Avg Turnaround Time": round(avg_turnaround, 2),
            "Avg Response Time": round(avg_response, 2),
            "CPU Utilization (%)": round(cpu_utilization, 2),
            "Throughput": round(throughput, 3)
        })

    comparison_df = pd.DataFrame(comparison)

    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )
    
    st.subheader("📥 Download Reports")

    # Download comparison report
    comparison_csv = comparison_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Comparison Report",
        data=comparison_csv,
        file_name="CPU_Scheduling_Comparison.csv",
        mime="text/csv"
    )

    # Download detailed process results
    detailed_results = []

    for algorithm, process_list in st.session_state.results.items():
        for process in process_list:
            detailed_results.append({
                "Algorithm": algorithm,
                **process
            })

    detailed_df = pd.DataFrame(detailed_results)

    detailed_csv = detailed_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Detailed Results",
        data=detailed_csv,
        file_name="CPU_Scheduling_Detailed_Results.csv",
        mime="text/csv"
    )


    st.subheader("📈 Gantt Charts")

    gantt_data = {}

    for name, result in st.session_state.results.items():

        if name == "Round Robin":
            gantt_data[name] = st.session_state.rr_gantt
        else:
            gantt_data[name] = [
                {
                    "pid": p["pid"],
                    "start": p["start"],
                    "end": p["completion"]
                }
                for p in result
            ]

    
    for name, schedule in gantt_data.items():

        st.write(f"**{name}**")

        fig, ax = plt.subplots(figsize=(10, 1.8))

        current_time = 0

        for item in schedule:

            start = item["start"]
            end = item["end"]

            # Show CPU idle time
            if start > current_time:
                idle_time = start - current_time

                ax.barh(
                    0,
                    idle_time,
                    left=current_time,
                    height=0.5,
                    color="lightgray",
                    edgecolor="black"
                )

                ax.text(
                    current_time + idle_time / 2,
                    0,
                    "IDLE",
                    ha="center",
                    va="center"
                )

            # Show process execution
            ax.barh(
                0,
                end - start,
                left=start,
                height=0.5,
                edgecolor="black"
            )

            ax.text(
                (start + end) / 2,
                0,
                item["pid"],
                ha="center",
                va="center"
            )

            current_time = end

        ax.set_xlabel("CPU Time")
        ax.set_yticks([])
        ax.set_xlim(left=0)
        ax.set_title(f"{name} Scheduling")

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)


        
    
    st.divider()
    st.header("🏆 Performance Analysis")

    st.write("### Best Algorithm by Metric")

    metrics = [
        "Avg Waiting Time",
        "Avg Turnaround Time",
        "Avg Response Time"
    ]

    for metric in metrics:
        best_index = comparison_df[metric].idxmin()
        best_algorithm = comparison_df.loc[
            best_index, "Algorithm"
        ]
        best_value = comparison_df.loc[
            best_index, metric
        ]

        st.success(
            f"{metric}: {best_algorithm} "
            f"({best_value})"
        )

    
    st.write("### Average Waiting Time Comparison")

    fig, ax = plt.subplots(figsize=(9, 4))

    algorithms = comparison_df["Algorithm"].tolist()
    waiting_times = comparison_df["Avg Waiting Time"].tolist()

    bars = ax.bar(
        algorithms,
        waiting_times
    )

    ax.set_ylabel("Average Waiting Time")
    ax.set_xlabel("Scheduling Algorithm")
    ax.set_title("Average Waiting Time Comparison")

    ax.bar_label(bars, fmt="%.2f", padding=4)

    ax.set_ylim(
        0,
        max(waiting_times) * 1.2 + 0.5
    )

    plt.xticks(rotation=15)
    plt.tight_layout()

    st.pyplot(fig)
    plt.close(fig)
