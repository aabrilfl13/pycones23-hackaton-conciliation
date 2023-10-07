import dotenv
import openai

dotenv.load_dotenv(dotenv_path=".env")

if __name__ == "__main__":
    user_present_situation = {
        "projects": [
            {
                "name": "Project 1",
                "start_date": "2023-10-10",
                "end_date": "2023-01-10",
                "hours_per_day": 2,
                "mandatory_meeting_time": "10:00 AM",
            },
            {
                "name": "Project 2",
                "start_date": "2023-09-01",
                "end_date": "2024-02-01",
                "hours_per_day": 2,
            },
            {
                "name": "Project 3",
                "start_date": "2023-09-01",
                "end_date": "2024-09-01",
                "hours_per_day": 4,
            },
        ],
        "working_hours": {
            "Monday": ["8:00 AM - 2:00 PM", "3:00 PM - 5:30 PM"],
            "Tuesday": ["8:00 AM - 2:00 PM", "3:00 PM - 5:30 PM"],
            "Wednesday": ["8:00 AM - 2:00 PM", "3:00 PM - 5:30 PM"],
            "Thursday": ["8:00 AM - 2:00 PM", "3:00 PM - 5:30 PM"],
            "Friday": ["8:00 AM - 2:00 PM", "3:00 PM - 5:30 PM"],
        },
    }

    output_example = """
        Actually you only have one work activity in progress. The tasks you have selected can be included in your schedule without any modification, in addition, it will not be necessary to add hours on the weekend.
        I propose the following days and hours to be able to work on them in the most optimal way:
        
        From Monday to Friday: From 12:00 to 14:30 you can work on the platform for Mercadona. From 16:00 to 18:00 you can work for the management of users for carrefour. From 18:30 to 20:00 you can spend the
        time having fun in basketball.
    """

    prompt_template = """
        You're an app that let me organize my personal time in the best way with work.
        I am an user that will add some projects or activities that consume my time
        during the day in a certain time and I want to see if I can do some studies or
        when to go to the gym.

        You must respect the hours that the user has already assigned for the activities.

        The output must be a propose of the best time to do the activities that the user wants to do.
        This is an example of the output:
            {output_example}
            
        Input will be a dictionary of the user present situation:
            {user_present_situation}

        User: I want to do the selected activities (work for mercadona, managing user for carrefour, play basketball) in a period of 3 months. Look for free slots adjusting to my schedule to be able to do them. Add weekends if necessary.
        Assistant:
        """

    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_template.format(
            output_example=output_example,
            user_present_situation=user_present_situation,
        ),
        temperature=0,
        max_tokens=1000,
    )

    print(completion.choices[0].text)
