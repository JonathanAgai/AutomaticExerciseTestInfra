# pythonProjectAutoTest

Adding a new exercise:

Early preparation work that will include:

Create a folder with the name of the exercise (hw<number>) that represents configurations and appendices of the exercise.
  
Inside a folder (hw<number>) we will create the following:
  
Creating a folder (lecturer_solution) containing the lecturer's solution (lecture_solution.py).
  
Preparation of a configuration file (gui_elements_locations.json) containing the names and location of the elements.
  
Preparation of a configuration file (tests_configurations.json) with a description of the elements,Features and tests.
  
exmaple Homework Exercise 1(can be viewed inside current code) :
  
  gui_elements_locations.json:
  ```json
  {
    "last_name": [20,45,93,30],
    "first_name":[20,75,93,30],
    "display_full_name": [70,117,150,37],
    "full_name": [20,169,93,30]
  }
  ```
  
  tests_configuration.json:
  ```json
  {
	"gui_elements": {
		"screen_width": 300,
		"screen_height": 200,
		"screen_offset_x": 15,
		"screen_offset_y": 15,

		"elements": {
			"last_name" : {
				"type": "label",
				"image_name": "last name.png",
				"input": {
					"orientation": "right",
					"width": 151,
					"height": 30
				}
			},
			"first_name" : {
				"type": "label",
				"image_name": "first name.png",
				"input": {
					"orientation": "right",
					"width": 151,
					"height": 30
				}
			},
			"full_name" : {
				"type": "label",
				"image_name": "full name.png",
				"input": {
					"orientation": "right",
					"width": 151,
					"height": 30
				}
			},
			"display_full_name": {
				"type": "button",
				"image_name": "display full name.png"
			}

		}
	},

	"features": {
		"display_name": {
			"display_name_with_only_last_name": {
				"operations": [
					{
						"click": "last_name-input"
					},
					{
						"keyboard": "Agai"
					},
					{
						"click": "display_full_name"
					},
					{
						"double_click": "last_name-input"
					},
					{
						"delete": ""
					}
				],
				"result": {
					"cropped_element_name": "full_name"
				}
			},
			"display_name_with_only_first_name": {
				"operations": [
					{
						"click": "first_name-input"
					},
					{
						"keyboard": "Yoni"
					},
					{
						"click": "display_full_name"
					}
				],
				"result": {
					"cropped_element_name": "full_name"
				}
			},
			"display_full_name": {
				"operations": [
					{
						"click": "last_name-input"
					},
					{
						"keyboard": "Agai"
					},
					{
						"click": "display_full_name"
					}
				],
				"result": {
					"cropped_element_name": "full_name"
				}
			}
		}
	}
}
```
  
Run a script (generate_hw_configurations) by entering the name of the exercise.
  
That will generate all the information needed to test an exercise.
  
Sample image after performing the steps:
  
  ![image](https://user-images.githubusercontent.com/69031468/170669949-450bfc77-d1ad-4387-936d-320c3107a478.png)
  
  
  
Product of the solution:
  
Images of the elements in the folder (gui_elements_images).
  
Pictures of the solution in a specific area tested in a folder (templates).
  
Full picture of the application after receiving the solution (application).
  
Existing exercise test:
  
Early preparation work that will include:
  
Create a folder (students_solution_exes)
  
Inside folder (students_solution_exes): Create a folder with the name of the exercise (hw<number>).
  
Inside a folder Within a folder (hw<number>) do the following:
  
Extracting student folders containing a executable file (student<id>.py)
  
Sample image after performing the steps:
  
  ![image](https://user-images.githubusercontent.com/69031468/170670264-51080cb4-c788-458f-a8ee-8ccf53b7b050.png)

  

Run the app and select an exercise and press the Run button.
  
Sample image:
  
  ![image](https://user-images.githubusercontent.com/69031468/170670370-e5c9ca8f-61a8-4cc0-aa9d-10b04b57e901.png)
 
After pressing the Run button the app will run each of the student programs and perform a test set and kill the program,
  
after completing all the runs the products will be:
  
  ![image](https://user-images.githubusercontent.com/69031468/170670506-7e0ff443-45af-479a-8e10-08a5a6c38b18.png)

  
A folder containing folders with the student's ID numbers containing pictures of that student's solution.
  
A file containing a detailed feedback report for all students.

  
  
  
  
  
  
