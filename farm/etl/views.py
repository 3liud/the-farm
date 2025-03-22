from django.shortcuts import render
import subprocess

def run_etl(request):
    result = subprocess.run(
        ["dagster", "job", "execute", "-f", "pipeline/pipeline.py"],
        capture_output=True, text=True
    )

    context = {
        'success': result.returncode == 0,
        'output': result.stdout if result.returncode == 0 else result.stderr
    }
    return render(request, 'etl_status.html', context)
