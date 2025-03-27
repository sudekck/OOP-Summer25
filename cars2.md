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
      "id": "39b10762-ac70-45ad-810d-3c56be51af8b",
      "cell_type": "code",
      "source": "### definition of class",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 1
    },
    {
      "id": "b0c718a0-605f-45d0-8120-e8e486f80b6c",
      "cell_type": "code",
      "source": "class Car:\n    def __init__(self,brand,model,year,type,color):\n        self.brand=brand\n        self.model=model\n        self.year=year\n        self.type=type\n        self.color=color\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 5
    },
    {
      "id": "675b9ffe-ccd8-4f46-ba2c-2d10a1c6a0bb",
      "cell_type": "code",
      "source": "c1=Car(\"bmw\",\"m4\",2024,\"sedan\",\"white\")\nprint(c1.brand)\nprint(c1.model)\nprint(c1.year)\nprint(c1.type)\nprint(c1.color)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "bmw\nm4\n2024\nsedan\nwhite\n"
        }
      ],
      "execution_count": 9
    },
    {
      "id": "bf85ade6-981f-4f96-8df8-1249c44b8ad7",
      "cell_type": "code",
      "source": "c2=Car(\"mercedes\",\"g400\",2022,\"jeep\",\"bronze\")\nprint(c2.brand)\nprint(c2.model)\nprint(c2.year)\nprint(c2.type)\nprint(c2.color)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "mercedes\ng400\n2022\njeep\nbronze\n"
        }
      ],
      "execution_count": 8
    },
    {
      "id": "883c180f-69d0-477d-a9d4-145c1bb87542",
      "cell_type": "code",
      "source": "c3=Car(\"volkswagen\",\"passat\",2021,\"sedan\",\"blue\")\nprint(c3.brand)\nprint(c3.model)\nprint(c3.year)\nprint(c3.type)\nprint(c3.color)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "volkswagen\npassat\n2021\nsedan\nblue\n"
        }
      ],
      "execution_count": 10
    },
    {
      "id": "ad3fc89e-e193-46eb-b3ee-c77318e65042",
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