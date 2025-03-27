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
      "id": "beaccbfb-ce35-4a9d-b312-e58ac03e12ad",
      "cell_type": "markdown",
      "source": "### definition of dictionary",
      "metadata": {}
    },
    {
      "id": "cc19c839-9144-4c5e-9d65-d1514ac9035a",
      "cell_type": "code",
      "source": "car1={\n    \"brand\":\"bmw\",\n    \"model\":\"m4\",\n    \"year\": 2024,\n    \"type\":\"sedan\",\n    \"color\":\"white\"\n}",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 2
    },
    {
      "id": "90af6cc1-1bb7-4314-96e4-a4e73db3dc36",
      "cell_type": "code",
      "source": "car2={\n    \"brand\":\"mercedes\",\n    \"model\":\"g400\",\n    \"year\":2022,\n    \"type\":\"jeep\",\n    \"color\":\"bronze\"\n}",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 3
    },
    {
      "id": "dd9675f5-5ac5-4b62-82dd-862f4005aeb0",
      "cell_type": "code",
      "source": "car3={\n    \"brand\":\"volkswagen\",\n    \"model\":\"passat\",\n    \"year\":2024,\n    \"type\":\"sedan\",\n    \"color\":\"blue\"\n}",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 4
    },
    {
      "id": "811fb72a-dd51-4088-a925-2e481ace3f2d",
      "cell_type": "markdown",
      "source": "### read values for car1",
      "metadata": {}
    },
    {
      "id": "b1d000a8-5a37-4f7c-b2f6-b7e4ef972a40",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "504f0c65-7faa-4589-bd9f-3f1a9fb31c28",
      "cell_type": "code",
      "source": "car1[\"brand\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 26,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'bmw'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 26
    },
    {
      "id": "e692f298-faba-46d9-8f81-0ada83500d0d",
      "cell_type": "code",
      "source": "car1[\"model\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 25,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'m4'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 25
    },
    {
      "id": "d650cfcf-7caa-4ae7-b470-f6c1e2344ee9",
      "cell_type": "code",
      "source": "car1[\"year\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 10,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2024"
          },
          "metadata": {}
        }
      ],
      "execution_count": 10
    },
    {
      "id": "8f9bfec0-1e79-4cfd-b424-5f5715e13760",
      "cell_type": "code",
      "source": "car1[\"type\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 11,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'sedan'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 11
    },
    {
      "id": "d08f795d-fef0-4e4c-bd60-e85b3377665d",
      "cell_type": "code",
      "source": "car1[\"color\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 12,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'white'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 12
    },
    {
      "id": "739b7fa9-1776-42ab-92fd-59888c227a91",
      "cell_type": "markdown",
      "source": "### read values for car2",
      "metadata": {}
    },
    {
      "id": "ef4655fd-5756-4716-9ae6-cec0741a5de7",
      "cell_type": "code",
      "source": "car2[\"brand\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'mercedes'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 13
    },
    {
      "id": "7ac23536-a15a-495b-8b7c-f6ea78c0df0c",
      "cell_type": "code",
      "source": "car2[\"model\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'g400'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 14
    },
    {
      "id": "edd66ca2-de34-4650-a843-f1b0cf7fb53b",
      "cell_type": "code",
      "source": "car2[\"year\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 15,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2022"
          },
          "metadata": {}
        }
      ],
      "execution_count": 15
    },
    {
      "id": "8ffb5bda-f43f-4191-8a7c-427a8e68435b",
      "cell_type": "code",
      "source": "car2[\"type\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 16,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'jeep'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 16
    },
    {
      "id": "1101ef60-b7e3-4889-a722-8101c05f53ab",
      "cell_type": "code",
      "source": "car2[\"color\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 17,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'bronze'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 17
    },
    {
      "id": "459b7738-9acb-4128-85ef-d6cefa8aa440",
      "cell_type": "markdown",
      "source": "### read values for car3",
      "metadata": {}
    },
    {
      "id": "32b581ca-9a4c-4f44-845a-c425093fd647",
      "cell_type": "code",
      "source": "car3[\"brand\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 18,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'volkswagen'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 18
    },
    {
      "id": "73a64242-8442-4a83-a735-cb13e4e2f60e",
      "cell_type": "code",
      "source": "car3[\"model\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 19,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'passat'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 19
    },
    {
      "id": "4bad6851-78b1-46d4-a37b-3f4e428108b3",
      "cell_type": "code",
      "source": "car3[\"year\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 20,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2024"
          },
          "metadata": {}
        }
      ],
      "execution_count": 20
    },
    {
      "id": "232693de-4925-4abe-8ea0-fd5aeb23463b",
      "cell_type": "code",
      "source": "car3[\"type\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 21,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'sedan'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 21
    },
    {
      "id": "ed4a4a59-57ca-4739-ac8e-cd5d4b88040c",
      "cell_type": "code",
      "source": "car3[\"color\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 22,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'blue'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 22
    },
    {
      "id": "67fc740a-43ff-43f1-a4e7-83ccb7087a3a",
      "cell_type": "markdown",
      "source": "### set values for car1",
      "metadata": {}
    },
    {
      "id": "2cd7d9a7-62d0-4daa-b914-3be3e2da62bb",
      "cell_type": "code",
      "source": "car1[\"brand\"]=\"bmw\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 28
    },
    {
      "id": "f235f820-fa0a-4b36-99a8-67878ee71b3c",
      "cell_type": "code",
      "source": "car1[\"brand\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 29,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'bmw'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 29
    },
    {
      "id": "cd51b7dd-5e35-44f1-9318-bb8867324b42",
      "cell_type": "code",
      "source": "car1[\"model\"]=\"m4\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 30
    },
    {
      "id": "96196964-542c-4873-83da-8b8e00def076",
      "cell_type": "code",
      "source": "car1[\"model\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 31,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'m4'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 31
    },
    {
      "id": "8af3e06f-9500-436c-8bf6-e1b7c4e05389",
      "cell_type": "code",
      "source": "car1[\"year\"]=2024",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 32
    },
    {
      "id": "8b8d4f5b-a726-44a3-a193-904c0f4ecd98",
      "cell_type": "code",
      "source": "car1[\"year\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 33,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2024"
          },
          "metadata": {}
        }
      ],
      "execution_count": 33
    },
    {
      "id": "7e7a839e-26fc-4f64-acb5-314f31c2f55f",
      "cell_type": "code",
      "source": "car1[\"type\"]=\"sedan\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 34
    },
    {
      "id": "4f579103-169d-46be-bd0c-e588b842c87f",
      "cell_type": "code",
      "source": "car1[\"type\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 35,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'sedan'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 35
    },
    {
      "id": "68af372f-5fc4-4935-863d-275f47bc2726",
      "cell_type": "code",
      "source": "car1[\"color\"]=\"white\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 36
    },
    {
      "id": "331ad3a8-a393-48b5-8aa0-fda120f7a1d5",
      "cell_type": "code",
      "source": "car1[\"color\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 37,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'white'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 37
    },
    {
      "id": "a4b667c5-c287-4bc0-97a2-74d24f319a00",
      "cell_type": "markdown",
      "source": "### set values for car2",
      "metadata": {}
    },
    {
      "id": "a0aa3e41-592a-447b-8b11-854d1d480445",
      "cell_type": "code",
      "source": "car2[\"brand\"]=\"mercedes\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 38
    },
    {
      "id": "a7899a1c-1fac-4edf-8af4-2db1311ba0bd",
      "cell_type": "code",
      "source": "car2[\"brand\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 39,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'mercedes'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 39
    },
    {
      "id": "2f6b1abc-2995-4790-b624-fbb4e5316d13",
      "cell_type": "code",
      "source": "car2[\"model\"]=\"g400\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 40
    },
    {
      "id": "5bedec25-6246-4546-8ac3-3fe45b25a1c8",
      "cell_type": "code",
      "source": "car2[\"model\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 41,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'g400'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 41
    },
    {
      "id": "8c724a94-1050-4579-b832-7439da4563a5",
      "cell_type": "code",
      "source": "car2[\"year\"]=2022",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 42
    },
    {
      "id": "29207019-0551-4aed-99c6-281c2027b5cc",
      "cell_type": "code",
      "source": "car2[\"year\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 43,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2022"
          },
          "metadata": {}
        }
      ],
      "execution_count": 43
    },
    {
      "id": "940e5ffa-cc04-41ab-bcd8-6082c18e5dcd",
      "cell_type": "code",
      "source": "car2[\"type\"]=\"jeep\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 44
    },
    {
      "id": "fcddab62-dcaf-4c64-8022-21aad1bba10e",
      "cell_type": "code",
      "source": "car2[\"type\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 45,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'jeep'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 45
    },
    {
      "id": "50391a07-853a-4a80-b991-f804fcd6a3fe",
      "cell_type": "code",
      "source": "car2[\"color\"]=\"bronze\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 46
    },
    {
      "id": "5512ead4-823c-4fb3-9a2e-31a7870067fa",
      "cell_type": "code",
      "source": "car2[\"color\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 47,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'bronze'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 47
    },
    {
      "id": "ca858a71-4db7-47e8-8b37-871f6b522226",
      "cell_type": "markdown",
      "source": "### set values for car3",
      "metadata": {}
    },
    {
      "id": "3f784956-74af-4930-be88-8d64c6794fe8",
      "cell_type": "code",
      "source": "car3[\"brand\"]=\"volkswagen\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 48
    },
    {
      "id": "5bce40bf-2eda-44bc-8837-bda4653c77a4",
      "cell_type": "code",
      "source": "car3[\"brand\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 49,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'volkswagen'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 49
    },
    {
      "id": "1f5ff51b-5fa9-40cd-b0a5-137f9becbd71",
      "cell_type": "code",
      "source": "car3[\"model\"]=\"passat\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 50
    },
    {
      "id": "7df976a1-9140-42da-8dc4-ce4c8a46de07",
      "cell_type": "code",
      "source": "car3[\"model\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 51,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'passat'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 51
    },
    {
      "id": "36224058-dde5-43d6-9f4a-d42e6091fb50",
      "cell_type": "code",
      "source": "car3[\"year\"]=2021",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 52
    },
    {
      "id": "9a7ac3c2-0b4f-4548-b91f-761d8c6155c3",
      "cell_type": "code",
      "source": "car3[\"year\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 53,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2021"
          },
          "metadata": {}
        }
      ],
      "execution_count": 53
    },
    {
      "id": "1d58b516-3b27-422a-938d-b7b83e87d6f2",
      "cell_type": "code",
      "source": "car3[\"type\"]=\"sedan\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 54
    },
    {
      "id": "4872e8e9-99fb-4a25-b219-3dc6d0f81948",
      "cell_type": "code",
      "source": "car3[\"type\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}