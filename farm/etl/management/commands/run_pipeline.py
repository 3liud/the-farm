from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = "Run Dagster ETL pipeline"

    def handle(self, *args, **kwargs):
        result = subprocess.run(["dagster", "job", "execute", "-f", "pipeline/pipeline.py"], capture_output=True, text=True)
        
        if result.returncode == 0:
            self.stdout.write(self.style.SUCCESS("Pipeline executed successfully"))
            self.stdout.write(result.stdout)
        else:
            self.stderr.write(self.style.ERROR("Pipeline execution failed"))
            self.stderr.write(result.stderr)
