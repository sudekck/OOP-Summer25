{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "f5dc988e-658a-48d1-a918-7388226d293c",
      "cell_type": "code",
      "source": "class Engine:\n    def __init__(self,horsepower,engine_type):\n        self.horsepower=horsepower\n        self.engine_type=engine_type\n\n\nclass Car:\n    def __init__(self,brand,model,year,type,color,engine):\n        self.brand=brand\n        self.model=model\n        self.year=year\n        self.type=type\n        self.color=color\n        self.engine=engine\n\ne1=Engine(400, \"v8\")\nc1=Car(\"bmw\",\"m4\",2024,\"sedan\",\"white\",e1)\nprint(c1.brand)\nprint(c1.model)\nprint(c1.year)\nprint(c1.type)\nprint(c1.color)\nprint(c1.engine.horsepower)\nprint(c1.engine.engine_type)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "bmw\nm4\n2024\nsedan\nwhite\n400\nv8\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "d8cb9ca0-2d2c-4987-b8cf-138a183fb51e",
      "cell_type": "code",
      "source": "e2=Engine(330, \"v6\")\nc2=Car(\"mercedes\",\"g400\",2022,\"jeep\",\"bronze\",e2)\nprint(c2.brand)\nprint(c2.model)\nprint(c2.year)\nprint(c2.type)\nprint(c2.color)\nprint(c2.engine.horsepower)\nprint(c2.engine.engine_type)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "mercedes\ng400\n2022\njeep\nbronze\n330\nv6\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "689bc0b4-122c-4703-ab1c-cb30689cc57b",
      "cell_type": "code",
      "source": "e3=Engine(150, \"inline4\")\nc3=Car(\"volkswagen\",\"passat\",2021,\"sedan\",\"blue\",e3)\nprint(c3.brand)\nprint(c3.model)\nprint(c3.year)\nprint(c3.type)\nprint(c3.color)\nprint(c3.engine.horsepower)\nprint(c3.engine.engine_type)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "volkswagen\npassat\n2021\nsedan\nblue\n150\ninline4\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "45abd1dd-2f44-42b0-9f5e-c08c8bac3dca",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}