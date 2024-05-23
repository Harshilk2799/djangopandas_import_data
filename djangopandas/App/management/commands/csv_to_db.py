import os
import pandas as pd
from django.conf import settings
from App.models import Student
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Import student from csv file"

    def handle(self, *args, **kwargs):

        # Define the path to the "demo" folder
        data_dir = os.path.join(settings.BASE_DIR, "demo")
        print(data_dir)

        # Create the full path to the csv file 
        csv_file_path = os.path.join(data_dir, "Test.csv")
        print(csv_file_path)

        try:
            # Load the CSV file into a DataFrame
            df = pd.read_csv(csv_file_path) 
            
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("CSV file not found."))
            return
        
        for _, row in df.iterrows():
            Student.objects.create(
                name=row["Name"],
                email=row["Email"],
                age=row["Age"]
            )

        self.stdout.write(self.style.SUCCESS("Successfully Imported students."))