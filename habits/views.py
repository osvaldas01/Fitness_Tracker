from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, HabitLog
from django.contrib import messages
from datetime import date
from .forms import UserRegistrationForm

# Add this new view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    total_habits = habits.count()
    weekly_completion_rate = sum(habit.completion_rate for habit in habits) / total_habits if total_habits > 0 else 0
    best_streak = max((habit.current_streak for habit in habits), default=0)
    
    context = {
        'habits': habits,
        'total_habits': total_habits,
        'weekly_completion_rate': round(weekly_completion_rate),
        'best_streak': best_streak,
    }
    return render(request, 'habits/habit_list.html', context)

@login_required
def habit_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        target_days = request.POST.get('target_days', 7)
        
        Habit.objects.create(
            user=request.user,
            name=name,
            description=description,
            target_days_per_week=target_days
        )
        return redirect('habits:habit_list')
    
    return render(request, 'habits/habit_add.html')

@login_required
def habit_log(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    
    if request.method == 'POST':
        completed = request.POST.get('completed') == 'on'
        notes = request.POST.get('notes', '')
        
        habit_log, created = HabitLog.objects.get_or_create(
            habit=habit,
            date=date.today(),
            defaults={'completed': completed, 'notes': notes}
        )
        
        if not created:
            habit_log.completed = completed
            habit_log.notes = notes
            habit_log.save()
            
        messages.success(request, 'Progress logged successfully!')
        return redirect('habits:habit_list')
        
    return render(request, 'habits/habit_log.html', {'habit': habit})

@login_required
def habit_delete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        messages.success(request, 'Habit deleted successfully!')
        return redirect('habits:habit_list')
    return render(request, 'habits/habit_delete.html', {'habit': habit})
