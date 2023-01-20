# ECE434 Homework 6
## What Every Driver Developer Should Know About RT
### Sophia Harrison 

## Watch
Answers:
1. Julia Cartwright works at National Instruments.
2. PREEMPT_RT is a patch that aims at making all code running in kernel mode preemptible, which is the ability to stop whatever the CPU is running to run another task. 
3. Mixed criticality is when you have both real-time critical tasks and non-time critical tasks. 
4. Drivers can misbehave whenever you have a lot of register writes back-to-back without a read, because the CPU cannot dispatch interrupts until it gets the read response back, because they are waiting for buffers to propagate down to the device and back, which causes delay due to architectural restraints.
5. Delta is the time between an event and the application. This delta is made up of the time it takes for an irq to dispatch and the time it takes for the task to be scheduled.
6. Cyclictest is test that accurately and repeatedly measures the difference between  thread’s intended wake-up time and the time at which it actually wakes up, which provides statistics about the system’s latencies.
7. Figure 2 shows the time it takes for a thread to actually sleep minus the intended duration of sleep for the thread (latency), data collected from cyclictest. Figure 2 is a histogram showing the latencies for preempt in mainline and also preempt_rt, where we can see preempt_rt has a better distribution more suitable for real time application. 
8. Dispatch latency is the amount of time it takes between the external hardware firing to the relevant thread being woken up. Scheduling latency is the amount of time it takes from the scheduler being made aware of a high priority task needing to be run to the CPU being given the actual task to be executed. 
9. Mainline is the main kernel tree. This is where all new kernel features are introduced. 
10. A non-critical irq is keeping the external event from starting in Figure 3, the external event cannot be scheduled until the irq is finished executing.
11. The external event in Figure 4 can start sooner because it uses the preempt_rt patch which allows forced IRQ threading. This means that when an IRQ is fired only a little code is actually run, just enough to wake up threads that will execute their respective handlers, allowing the high priority external event to start sooner.

## PREEMPT_RT
In order to test the kernel's performance, I created a bash file that acts as the load (see loadtest.sh) for the loaded portion of the test. The loadtest.sh bash file contains the commands make and make clean which run in an infinite loop. I ran the cyclic test on the regular kernel without the load and then with the load and got the respective data. I then ran the same test with and without a load for the real time kernel. I was using kernel versions 5.10.140-ti-r52 and 5.10.140-ti-rt-r52 for this part. 
<br>
For the unloaded test, it appears both kernels have about the same performance and have a bound around 100 microseconds. Seen in cyclictest_noload.png
<img src=/cyclictest_noload.png>
<br>
For the loaded test, the real time kernel has about the same performace as it did with no load, with a bound still around 100 microseconds. The non-rt kernel had worse performance with the load compared to when it had no load, and the bound of its performance is harder to distinguish. See cyclictest_load.png
<img src=/cylictest_load.png>
