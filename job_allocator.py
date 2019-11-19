# Data:
# Tasks queue is a list
# Job represented by a dictionary
# Worker repr by dictionary
from operator import itemgetter

class Type: 
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


class Task: 
    def __init__(self, jobtype, weighting=1):
        self.jobtype = jobtype
        self.weighting = weighting 
        self.done = False


class Worker:
    def __init__(self, skills, penalty):
        self.skills = skills
        self.penalty = penalty
        self.task = None
        self.fatigue = 1        ## not implemented
        self.busy = 0           ## semaphore

    def is_penalty(self, task):
        return - int(self.penalty in task.jobtype.skills)

    def skill_score(self, task):
        ## list all the matched skills
        skill_match = len(set(task.jobtype.skills).intersection(self.skills))
        # skill_match = set(task.jobtype.skills) & set(self.skills)
        ## testing if penalty exists
        score = skill_match + self.is_penalty(task)
        return score

    def compute_duration(self, task):
        duration = task.weighting * (100 - (5 * max(0, self.skill_score(task)) ** 1.5)) / (100 * (self.fatigue))
        return round(duration)


class Scheduler:
    def __init__(self, ):
        self.fifo = []

    def run_tasks(self):
        for task in list(self.fifo):
            ## finding the best available worker
            best_duration = 10000
            best_worker = None
            for name, worker in workers.items():
                contender_duration = worker.compute_duration(task)
                if None == worker.task and contender_duration < best_duration:
                    best_name, best_worker = name, worker
                    best_duration = contender_duration

            if best_worker == None:
                print('no worker available')
                return 

            best_worker.task = task
            best_worker.busy += best_duration
            self.fifo.remove(task)
            print(f"task '{task.jobtype.name}' started with \tworker '{best_name}' \tfor duration '{best_duration}'")

    def step(self):
        for k, v in workers.items():
            v.busy = max(0, v.busy -1)
            if v.busy < 1 : 
                v.task = None
                v.fatigue = min(1, v.fatigue + 0.1)
            else:
                v.fatigue *= .9
        self.run_tasks()

## job types
job_types = {        
    'music': Type('Playing music', ['creativity', 'coordination', 'drinking']),
    'kicking_ball': Type('Kicking a ball', ['energy', 'coordination', 'determination']),
    'software': Type('Writing Software', ['logic','determination','vision']),
    'space_travel': Type('Going to Space', ['determination', 'logic', 'curiosity']),
    'dig_tunnel': Type('Dig a tunnel', ['energy', 'determination', 'curiosity']),
    'daydreaming': Type('Daydreaming', ['creativity', 'drinking', 'communication']),
    'cold': Type('Catching a Cold', ['energy', 'drinking', 'communication']),
}

## workers
workers = {
    'student': Worker(['drinking', 'curiosity', 'energy'], 'communication'),
    'engineer': Worker(['logic', 'vision', 'creativity'], 'coordination'),
    'lawyer': Worker(['communication', 'determination', 'vision'], 'drinking'),
    'mathematician': Worker(['logic', 'vision', 'determination'], 'coordination'),
    'artist': Worker(['creativity', 'coordination', 'drinking'], 'logic'),
    'barista': Worker(['coordination', 'communication', 'drinking'], 'energy'),
}


## if main
if __name__ == "__main__":
    from random import choice, randint
    from time import sleep
    task1 = Task(job_types['software'], 2)
    task2 = Task(job_types['music'], 3)
    scheduler = Scheduler()
    N = 5
    while(True):
        ## generate N random tasks
        for _ in range(randint(0, N)):
            rand_task = choice(list(job_types.keys()))
            next_task = Task(job_types[rand_task], randint(1, 3))
            
            scheduler.fifo.append(next_task)
        
        scheduler.step() 
        ## sleep 1 sec
        sleep(1)


##################################
# from job_allocator import *
# task1 = Task(job_types['software'], 2)
# task2 = Task(job_types['music'], 3)