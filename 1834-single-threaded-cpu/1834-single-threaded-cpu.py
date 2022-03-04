from heapq import heappush, heappop, heapify
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # time complexity = nlogn
        # space complexity = n -> heap
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        h = []
        nextTaskProcessTime = tasks[0][0]
        # timeWhenCPUwillbeidleNext = currTime + processing time
        while len(res) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= nextTaskProcessTime):
                heapq.heappush(h, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
                i += 1
            if h:
                processing_time, original_index = heapq.heappop(h)
                nextTaskProcessTime += processing_time
                res.append(original_index)
            # if there are no available tasks and CPU is idle 
            # move to the next task
            elif i < len(tasks):
                nextTaskProcessTime = tasks[i][0]
        return res
# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         tasksHeap = []
#         orderOfTasks = []
#         maxEnqueueTime = 0
#         minEnqueueTime = float('inf')
#         heapify(tasksHeap)
#         tasksAvailableAtEnqueueTime = collections.defaultdict(list)
#         sumOfProcessingTimes = 0
#         for i, task in enumerate(tasks):
#             tasksAvailableAtEnqueueTime[task[0]].append(i)
#             if task[0] < minEnqueueTime:
#                 minEnqueueTime = task[0]
#             if task[0] > maxEnqueueTime:
#                 maxEnqueueTime = task[0]
#             sumOfProcessingTimes += task[1]
#         tLimit = max(maxEnqueueTime , sumOfProcessingTimes + minEnqueueTime)
#         # at t= 0 CPU is idle or infact CPU is idle until minimum enqueue time
#         timeCPUWillBecomeIdle = 0
#         for t in range(0,tLimit + 1):
#             if t in tasksAvailableAtEnqueueTime:
#                 for i in tasksAvailableAtEnqueueTime[t]:
#                     heappush(tasksHeap, (tasks[i][1], i))
#             if t >= timeCPUWillBecomeIdle and tasksHeap:
#                 processingTime, index = heappop(tasksHeap)
#                 timeCPUWillBecomeIdle = t + processingTime
#                 orderOfTasks.append(index)
        
#         return orderOfTasks

		