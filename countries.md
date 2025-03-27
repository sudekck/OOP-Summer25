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
      "id": "afc94bd4-ae38-4db2-a779-55af9eb8f95b",
      "cell_type": "markdown",
      "source": "### dict definition 1",
      "metadata": {}
    },
    {
      "id": "4157c984-1cb4-4cef-b815-f958491c094d",
      "cell_type": "code",
      "source": "countries1 = {\n    \"name\": \"canada\",\n    \"population\": \"40,1 million\",\n    \"continent\": \"america\",\n    \"capital_city\": \"ottawa\",\n    \"3_biggest_cities\": [\"toronto\",\"montreal\",\"calgary\"]\n}",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 9
    },
    {
      "id": "4140a02f-4bc6-4cd9-805e-94cc3346c69e",
      "cell_type": "markdown",
      "source": "### read values",
      "metadata": {}
    },
    {
      "id": "0f3861ed-cf2e-4d5c-97ac-738e9957f1fc",
      "cell_type": "code",
      "source": "print(countries1[\"name\"])",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "canada\n"
        }
      ],
      "execution_count": 10
    },
    {
      "id": "7f89952b-1e1c-443d-90e3-92b3f18e7e0d",
      "cell_type": "code",
      "source": "countries1[\"population\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 11,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'40,1 million'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 11
    },
    {
      "id": "e00e0a16-1df8-4b3e-b742-fe29bbe2325d",
      "cell_type": "code",
      "source": "countries1[\"continent\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 12,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'america'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 12
    },
    {
      "id": "41763feb-3564-4008-8d2e-7612daa96b42",
      "cell_type": "code",
      "source": "countries1[\"capital_city\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'ottowa'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 13
    },
    {
      "id": "7a14c5b4-86b7-4b16-97e3-6933fb397476",
      "cell_type": "code",
      "source": "countries1[\"3_biggest_cities\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "['toronto', 'montreal', 'calgary']"
          },
          "metadata": {}
        }
      ],
      "execution_count": 14
    },
    {
      "id": "ed4839ac-830b-426e-8b5f-d3554bafdc3d",
      "cell_type": "markdown",
      "source": "### set values",
      "metadata": {}
    },
    {
      "id": "80c879eb-ecb5-4c2a-8b23-0f8d8f5acc4a",
      "cell_type": "code",
      "source": "countries1[\"name\"] = \"canada\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "36392206-301a-4456-a1c4-c1e64a91e35e",
      "cell_type": "code",
      "source": "countries1[\"name\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 15,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'canada'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 15
    },
    {
      "id": "6ffe18fc-9b8d-4688-a3a9-cd395147cca9",
      "cell_type": "markdown",
      "source": "### dict definition 2",
      "metadata": {}
    },
    {
      "id": "b44bba7e-627a-46e9-b129-13fa1fb4ecee",
      "cell_type": "code",
      "source": "countries2={\n    \"name\":\"turkiye\",\n    \"population\":\"85,33 million\",\n    \"continent\":\"asia\",\n    \"capital_city\":\"ankara\",\n    \"3_biggest_cities\":[\"istanbul\",\"ankara\",\"izmir\"]\n}",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 17
    },
    {
      "id": "b5a1675d-4c4f-4fb6-9ee0-be5e7eb711b7",
      "cell_type": "markdown",
      "source": "### read values",
      "metadata": {}
    },
    {
      "id": "eb8fd78a-a2b9-44b1-96f6-d89e39daeb1b",
      "cell_type": "code",
      "source": "countries2[\"name\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 18,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'turkiye'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 18
    },
    {
      "id": "d13f0cb1-4db6-4581-a473-2394aed26a5e",
      "cell_type": "code",
      "source": "countries2[\"population\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 20,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'85,33 million'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 20
    },
    {
      "id": "f627c486-56cc-466a-a267-0cd790fe3892",
      "cell_type": "code",
      "source": "countries2[\"continent\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 21,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'asia'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 21
    },
    {
      "id": "dc4d88a3-4a2f-4636-8814-59a177942d7e",
      "cell_type": "code",
      "source": "countries2[\"capital_city\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 22,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'ankara'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 22
    },
    {
      "id": "5b86b219-57f9-440f-8a60-47888ebb4d96",
      "cell_type": "code",
      "source": "countries2[\"3_biggest_cities\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 23,
          "output_type": "execute_result",
          "data": {
            "text/plain": "['istanbul', 'ankara', 'izmir']"
          },
          "metadata": {}
        }
      ],
      "execution_count": 23
    },
    {
      "id": "2e9ce12c-42f0-434b-9078-060f6762fee3",
      "cell_type": "markdown",
      "source": "### set values",
      "metadata": {}
    },
    {
      "id": "d1ab7589-911d-47ab-a5d6-551f2445a19e",
      "cell_type": "code",
      "source": "countries2[\"name\"]=\"turkiye\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 24
    },
    {
      "id": "53268e52-5b8a-4fc4-98e5-f0de4c5299c1",
      "cell_type": "code",
      "source": "countries2[\"name\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 25,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'turkiye'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 25
    },
    {
      "id": "96d18773-7668-407f-887c-8f8cb2c0594c",
      "cell_type": "markdown",
      "source": "### dict definition 3",
      "metadata": {}
    },
    {
      "id": "5b352d60-6b5b-4475-b050-a526a7f932e0",
      "cell_type": "code",
      "source": "countries3={\n    \"name\":\"poland\",\n    \"population\":\"36,69 million\",\n    \"continent\":\"europe\",\n    \"capital_city\":\"warsaw\",\n    \"3_biggest_cities\":[\"warsaw\",\"krakow\",\"Łódź\"]\n}",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 26
    },
    {
      "id": "bc53fc1e-1d75-4007-bd18-875c53170918",
      "cell_type": "markdown",
      "source": "### read values",
      "metadata": {}
    },
    {
      "id": "961b8fe2-eb5c-427e-8986-936b6da20ae1",
      "cell_type": "code",
      "source": "countries3[\"name\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 27,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'poland'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 27
    },
    {
      "id": "f12f215b-74ac-4da2-b73f-20e597fae6bb",
      "cell_type": "code",
      "source": "countries3[\"population\"]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 28,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'36,69 million'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 28
    },
    {
      "id": "179f44a5-6efc-400b-a37f-ef40eb89740b",
      "cell_type": "code",
      "source": "countries3[",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}