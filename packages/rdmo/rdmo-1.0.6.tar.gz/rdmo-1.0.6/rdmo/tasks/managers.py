from django.db import models


class TaskManager(models.Manager):

    def active_by_project(self, project):
        tasks = []

        for task in self.get_queryset():
            conditions = task.conditions.all()

            if conditions:
                for condition in conditions:
                    if condition.resolve(project):
                        tasks.append(task)
                        break

                task.dates = task.get_dates(project)

        return tasks
