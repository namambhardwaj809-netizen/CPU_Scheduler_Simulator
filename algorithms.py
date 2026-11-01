
def fcfs(processes):
    processes = sorted(processes, key=lambda p: p["arrival"])

    current_time = 0
    results = []

    for process in processes:
        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        start_time = max(current_time, arrival)
        completion_time = start_time + burst

        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = start_time - arrival

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time,
            "response": response_time
        })

        current_time = completion_time

    return results

def sjf(processes):
    processes = sorted(processes, key=lambda p: p["arrival"])

    current_time = 0
    remaining = processes.copy()
    results = []

    while remaining:
        available = [
            p for p in remaining
            if p["arrival"] <= current_time
        ]

        if not available:
            current_time = remaining[0]["arrival"]
            continue

        process = min(available, key=lambda p: p["burst"])

        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        start_time = current_time
        completion_time = start_time + burst

        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = start_time - arrival

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time,
            "response": response_time
        })

        current_time = completion_time
        remaining.remove(process)

    return results

def priority_scheduling(processes):
    processes = sorted(processes, key=lambda p: p["arrival"])

    current_time = 0
    remaining = processes.copy()
    results = []

    while remaining:
        available = [
            p for p in remaining
            if p["arrival"] <= current_time
        ]

        if not available:
            current_time = remaining[0]["arrival"]
            continue

        process = min(
            available,
            key=lambda p: (p["priority"], p["arrival"])
        )

        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        start_time = current_time
        completion_time = start_time + burst

        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = start_time - arrival

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": process["priority"],
            "start": start_time,
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time,
            "response": response_time
        })

        current_time = completion_time
        remaining.remove(process)

    return results


from collections import deque


def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda p: p["arrival"])

    remaining = {
        p["pid"]: p["burst"] for p in processes
    }

    first_start = {}
    completion = {}
    gantt = []

    ready_queue = deque()
    current_time = 0
    index = 0

    while index < len(processes) or ready_queue:

        if not ready_queue and index < len(processes):
            current_time = max(
                current_time, processes[index]["arrival"]
            )

        while (index < len(processes)
               and processes[index]["arrival"] <= current_time):
            ready_queue.append(processes[index])
            index += 1

        if not ready_queue:
            continue

        process = ready_queue.popleft()
        pid = process["pid"]

        if pid not in first_start:
            first_start[pid] = current_time

        start = current_time
        execution = min(quantum, remaining[pid])

        current_time += execution
        remaining[pid] -= execution

        gantt.append({
            "pid": pid,
            "start": start,
            "end": current_time
        })

        while (index < len(processes)
               and processes[index]["arrival"] <= current_time):
            ready_queue.append(processes[index])
            index += 1

        if remaining[pid] > 0:
            ready_queue.append(process)
        else:
            completion[pid] = current_time

    results = []

    for p in processes:
        pid = p["pid"]
        turnaround = completion[pid] - p["arrival"]

        results.append({
            "pid": pid,
            "arrival": p["arrival"],
            "burst": p["burst"],
            "start": first_start[pid],
            "completion": completion[pid],
            "waiting": turnaround - p["burst"],
            "turnaround": turnaround,
            "response": first_start[pid] - p["arrival"]
        })

    return results, gantt




if __name__ == "__main__":
    processes = [
        {"pid": "P1", "arrival": 0, "burst": 5},
        {"pid": "P2", "arrival": 1, "burst": 3},
        {"pid": "P3", "arrival": 2, "burst": 2},
    ]

    result, gantt = round_robin(processes, quantum=2)

    print("Round Robin Results:")

    for process in result:
        print(process)

    print("\nGantt Chart:")
    for item in gantt:
        print(item)

