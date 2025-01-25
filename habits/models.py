from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    target_days_per_week = models.IntegerField(default=7)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def logged_today(self):
        return self.habitlog_set.filter(date=date.today()).exists()
    
    @property
    def latest_log(self):
        return self.habitlog_set.order_by('-date').first()
    
    @property
    def completion_rate(self):
        logs = self.habitlog_set.filter(
            date__gte=date.today() - timedelta(days=7)
        ).count()
        return round((logs / 7) * 100)
    
    @property
    def current_streak(self):
        logs = self.habitlog_set.filter(completed=True).order_by('-date')
        if not logs.exists():
            return 0
            
        streak = 0
        current_date = date.today()
        
        for log in logs:
            if log.date == current_date:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break
        return streak

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['habit', 'date']
