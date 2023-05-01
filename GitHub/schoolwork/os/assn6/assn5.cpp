#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

struct Process {
    int id, start_time, duration, remaining_time, wait_time, response_time, turnaround_time;
};

bool compare_arrival_time(const Process& a, const Process& b) {
    return a.start_time < b.start_time;
}

bool compare_duration(const Process& a, const Process& b) {
    return a.duration < b.duration;
}

bool compare_remaining_time(const Process& a, const Process& b) {
    return a.remaining_time < b.remaining_time;
}

void calculate_avg_times(const std::vector<Process>& processes, double& avg_response_time, double& avg_turnaround_time, double& avg_wait_time) {
    int n = processes.size();
    double total_response_time = 0, total_turnaround_time = 0, total_wait_time = 0;

    for (const auto& process : processes) {
        total_response_time += process.response_time;
        total_turnaround_time += process.turnaround_time;
        total_wait_time += process.wait_time;
    }

    avg_response_time = total_response_time / n;
    avg_turnaround_time = total_turnaround_time / n;
    avg_wait_time = total_wait_time / n;
}

std::vector<Process> first_come_first_served(std::vector<Process> processes) {
    std::sort(processes.begin(), processes.end(), compare_arrival_time);
    int current_time = 0;

    for (auto& process : processes) {
        if (current_time < process.start_time) {
            current_time = process.start_time;
        }
        process.response_time = current_time - process.start_time;
        process.wait_time = process.response_time;
        current_time += process.duration;
        process.turnaround_time = current_time - process.start_time;
    }

    return processes;
}

std::vector<Process> shortest_job_first(std::vector<Process> processes) {
    std::sort(processes.begin(), processes.end(), compare_arrival_time);
    std::priority_queue<Process, std::vector<Process>, decltype(compare_duration)*> pq(compare_duration);
    std::vector<Process> completed_processes;
    int current_time = 0, i = 0;

    while (!processes.empty() || !pq.empty()) {
        while (i < processes.size() && processes[i].start_time <= current_time) {
            pq.push(processes[i]);
            processes.erase(processes.begin() + i);
        }

        if (!pq.empty()) {
            auto process = pq.top();
            pq.pop();
            process.response_time = current_time - process.start_time;
            process.wait_time = process.response_time;
            current_time += process.duration;
            process.turnaround_time = current_time - process.start_time;
            completed_processes.push_back(process);
        } else {
            current_time++;
        }
    }

    return completed_processes;
}

std::vector<Process> shortest_remaining_time_first(std::vector<Process> processes) {
    std::sort(processes.begin(), processes.end(), compare_arrival_time);
    std::vector<Process> completed_processes;
    std::priority_queue<Process, std::vector<Process>, decltype(&compare_remaining_time)> pq(compare_remaining_time);
    int current_time = 0, i = 0;

    while (!processes.empty() || !pq.empty()) {
        while (i < processes.size() && processes[i].start_time <= current_time) {
            processes[i].remaining_time = processes[i].duration;
            pq.push(processes[i]);
            i++;
        }

        if (!pq.empty()) {
            auto process = pq.top();
            pq.pop();
            process.response_time = current_time - process.start_time;
            current_time++;
            process.remaining_time--;
            if (process.remaining_time == 0) {
                process.turnaround_time = current_time - process.start_time;
                process.wait_time = process.turnaround_time - process.duration;
                completed_processes.push_back(process);
                processes.erase(processes.begin(), processes.begin() + i);
                i = 0;
            } else {
                pq.push(process);
            }
        } else {
            current_time++;
        }
    }

    return completed_processes;
}
std::vector<Process> round_robin(std::vector<Process> processes, int time_quantum) {
    std::sort(processes.begin(), processes.end(), compare_arrival_time);
    std::queue<Process> q;
    std::vector<Process> completed_processes;
    int current_time = 0, i = 0;

    while (!processes.empty() || !q.empty()) {
        while (i < processes.size() && processes[i].start_time <= current_time) {
            processes[i].remaining_time = processes[i].duration;
            q.push(processes[i]);
            processes.erase(processes.begin() + i);
        }

        if (!q.empty()) {
            auto process = q.front();
            q.pop();
            if (process.response_time == -1) {
                process.response_time = current_time - process.start_time;
            }
            int time_slice = std::min(time_quantum, process.remaining_time);
            current_time += time_slice;
            process.remaining_time -= time_slice;

            if (process.remaining_time == 0) {
                process.turnaround_time = current_time - process.start_time;
                process.wait_time = process.turnaround_time - process.duration;
                completed_processes.push_back(process);
            } else {
                q.push(process);
            }
        } else {
            current_time++;
        }
    }

    return completed_processes;
}

int main() {
    std::vector<Process> processes;
    int start_time, duration;
    int process_id = 0;

    while (std::cin >> start_time >> duration) {
        processes.push_back({process_id++, start_time, duration, -1, -1, -1, -1});
    }

    std::vector<Process> fcfs_result = first_come_first_served(processes);
    std::vector<Process> sjf_result = shortest_job_first(processes);
    std::vector<Process> srtf_result = shortest_remaining_time_first(processes);
    std::vector<Process> rr_result = round_robin(processes, 100);

    double fcfs_resp, fcfs_ta, fcfs_wait, sjf_resp, sjf_ta, sjf_wait, srtf_resp, srtf_ta, srtf_wait, rr_resp, rr_ta, rr_wait;
    calculate_avg_times(fcfs_result, fcfs_resp, fcfs_ta, fcfs_wait);
    calculate_avg_times(sjf_result, sjf_resp, sjf_ta, sjf_wait);
    calculate_avg_times(srtf_result, srtf_resp, srtf_ta, srtf_wait);
    calculate_avg_times(rr_result, rr_resp, rr_ta, rr_wait);

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "First Come, First Served\nAvg. Resp.:" << fcfs_resp << ", Avg. T.A.:" << fcfs_ta << ", Avg. Wait:" << fcfs_wait << std::endl;
    std::cout << "Shortest Job First\nAvg. Resp.:" << sjf_resp << ", Avg. T.A.:" << sjf_ta << ", Avg. Wait:" << sjf_wait << std::endl;
    std::cout << "Shortest Remaining Time First\nAvg. Resp.:" << srtf_resp << ", Avg. T.A.:" << srtf_ta << ", Avg. Wait:" << srtf_wait << std::endl;
    std::cout << "Round Robin with Time Quantum of 100\nAvg. Resp.:" << rr_resp << ", Avg. T.A.:" << rr_ta << ", Avg. Wait:" << rr_wait << std::endl;

    return 0;
}
