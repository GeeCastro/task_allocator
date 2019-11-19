# task_allocator
python dojo bristol nov 2019. Implement a simple solution that allocates tasks to workers.

## Problem
We decided to implement a task management system that allocates tasks (play music, write code, dig a tunnel) to workers (Artists, coders, engineers...). Each tasks requires skills and each worker has certain skills and a penalty: a skill she/he is not good at. Each macthing skill will increase a worker's score but a penalty will decrease its score. A scheduler will allocate tasks to the best worker (with the highest score) available for the next task (FIFO stack).

## Solution
The programme is composed of tasks, types (of tasks), workers, skills and the scheduler.

