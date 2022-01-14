# Differential Equantions Practicum

The full description of the project is accessible via the [following link](https://humdrum-cardboard-41e.notion.site/DE-Computational-Practicum-b5d98074cabf49eda1a0cddae9046caa) (Notion).

I developed a program that solves the problem below numerically and compares it to the analytical solution.

![image](https://user-images.githubusercontent.com/48735488/149514259-315018e5-4cac-4db6-bc6d-3817ab29bb08.png)

## Tools Used

- Programming Language: Python 3.9.7
- GUI Framework: PyQt5
- Libraries: Matplotlib + NumPy
- IDE: Microsoft Visual Studio Code
- Qt Designer

## Description of the program

### Plotted Graphs

- The exact solution of the IVP (conditions are specified by the user)
- The solution approximation using the explicit Euler method
- The solution approximation using the improved Euler method
- The solution approximation using the Runge-Kutta method
- The local truncation error for each of the three numerical methods listed above
- The global truncation error for each of the three numerical methods listed above

### Implemented Features

- The possibility to change the IVP conditions: $x_0, y_0, X$
- The possibility to change the number of grid steps $N$ (hence to control the step size $h$)
- The possibility to change the range of grid steps $[n_0,N]$ for the GTE graph
- Incorrect input handling with notifying of the user
- The possibility to manipulate each graph (panning, zooming, taking screenshots)

## GUI and Results

![image](https://user-images.githubusercontent.com/48735488/149515020-dc35d1a5-dab2-4d8f-a14c-0c93a03c9c9f.png)

![image](https://user-images.githubusercontent.com/48735488/149515055-37587f66-9131-4888-aae1-848dc5b5127f.png)

## UML diagram and Code Snippets

### MVC Pattern

The program implements the MVC software design pattern. It allows dividing the program logic into three interconnected elements: Model, View, and Controller. As a result, the user doesn't have access to the internal representations of the model parts (functions, numerical methods, etc.), and the model doesn't have direct access to the GUI. The developer can work independently on each component of the system, and modify it seamlessly.

![image](https://user-images.githubusercontent.com/48735488/149515924-cc2c5ab0-2c51-4f2b-beda-3f1468f29aaf.png)

The full UML diagram is accessible via the [following link](https://drive.google.com/file/d/1BdUVslKDe8lsG8E9p0F3aTxw7oU44NuU/view?usp=sharing) (draw.io service).
