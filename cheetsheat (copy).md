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
      "id": "a1c0e25c-8931-4ae5-8833-63e786fbcc73",
      "cell_type": "markdown",
      "source": "Python Cheetsheat",
      "metadata": {}
    },
    {
      "id": "ceba05b0-8faa-4116-912e-356f3f8a756b",
      "cell_type": "markdown",
      "source": "### Variables",
      "metadata": {}
    },
    {
      "id": "dfb4af07-ef32-46ed-adb9-befb5e22861f",
      "cell_type": "code",
      "source": "x = 18",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "aa298561-3b68-4039-af13-de8f407f653b",
      "cell_type": "code",
      "source": "y = \"Object-Oriented Programming\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 3
    },
    {
      "id": "9b08f277-f01d-4d22-85db-c9d110a95e01",
      "cell_type": "markdown",
      "source": "### Data Types",
      "metadata": {}
    },
    {
      "id": "3d8d6588-0314-4532-93ec-847935c2b1ed",
      "cell_type": "code",
      "source": "x = 1 #integer",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 6
    },
    {
      "id": "12f89873-e223-4061-8d99-0f3fcf327e98",
      "cell_type": "code",
      "source": "type(x)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 7,
          "output_type": "execute_result",
          "data": {
            "text/plain": "int"
          },
          "metadata": {}
        }
      ],
      "execution_count": 7
    },
    {
      "id": "01d7b2dd-63fc-4f0f-8a2d-a72d5230e987",
      "cell_type": "code",
      "source": "y = \"Sude\"\ntype(y)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 8,
          "output_type": "execute_result",
          "data": {
            "text/plain": "str"
          },
          "metadata": {}
        }
      ],
      "execution_count": 8
    },
    {
      "id": "6fa2222b-ea5d-4795-b683-0ac7e7fb1cdb",
      "cell_type": "code",
      "source": "z = [1,2,3] \ntype(z)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 9,
          "output_type": "execute_result",
          "data": {
            "text/plain": "list"
          },
          "metadata": {}
        }
      ],
      "execution_count": 9
    },
    {
      "id": "edc00b35-5c38-4b06-b129-c223484eaa34",
      "cell_type": "code",
      "source": "c = {\"name\": \"sude\", \"age\": \"22\"}\ntype(c)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 11,
          "output_type": "execute_result",
          "data": {
            "text/plain": "dict"
          },
          "metadata": {}
        }
      ],
      "execution_count": 11
    },
    {
      "id": "d6de8974-bb59-4823-81d5-0746207ebcc7",
      "cell_type": "code",
      "source": "b = (23,45,67)\ntype(b)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 12,
          "output_type": "execute_result",
          "data": {
            "text/plain": "tuple"
          },
          "metadata": {}
        }
      ],
      "execution_count": 12
    },
    {
      "id": "ec3a4eff-ea9d-44a2-bcac-0dd41a7e33a2",
      "cell_type": "code",
      "source": "d = {12,45,78}\ntype(d)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "set"
          },
          "metadata": {}
        }
      ],
      "execution_count": 13
    },
    {
      "id": "b2ce8ca2-b12f-46b5-8101-2744f3e14e29",
      "cell_type": "code",
      "source": "true_or_false = True\ntype(true_or_false)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "bool"
          },
          "metadata": {}
        }
      ],
      "execution_count": 14
    },
    {
      "id": "64b92cdc-cf16-4c6b-8563-88b8828ab367",
      "cell_type": "markdown",
      "source": "### Append Method",
      "metadata": {}
    },
    {
      "id": "a8b63044-03a9-4a86-8c7e-c5babe3a6935",
      "cell_type": "markdown",
      "source": "first define a function:\ndef main_function_name(it's elements):\n    main_function = { \"element1\": element1, \"element2\": element2}->write them as dict\n    main_function.append(main_function)\n    print(what you wanna print)",
      "metadata": {}
    },
    {
      "id": "c36e08df-5176-4fc6-b97d-38c03338ca0a",
      "cell_type": "markdown",
      "source": "### Creating a Class",
      "metadata": {}
    },
    {
      "id": "26563cac-d139-47a0-81da-e36d7049a6dd",
      "cell_type": "code",
      "source": "first:\nclass Person:\n    def __init__(self,thing1,thing2,...):\n        self.thing1=thing1\n        self.thing2=thing2\n        self.thing3=thing3\np1=Person(\"thing1\",thing2(if its a int),\"thing3\")\nprint(p1.thing1)\nprint(p1.thing2)\n    .\n    .\n    .",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "d84cd275-497a-4540-a0fe-27f9adbb6a0c",
      "cell_type": "markdown",
      "source": "### Creating a Loop",
      "metadata": {}
    },
    {
      "id": "e2adf1ed-c778-455d-82d5-aceee6fea497",
      "cell_type": "code",
      "source": "use for loop(example from exercise with students)\nfor student in students:\n    print(f\"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}\")\n\nf string-formatted string literals/first message and then variable that we assigned\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "da7494d8-2347-4a2a-a550-9534a8edf11d",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "7cc622ec-42ad-4424-bbec-97dd2293b2d8",
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