{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fefd7252-4f02-4bec-9fd7-d2d24c66e122",
      "metadata": {
        "id": "fefd7252-4f02-4bec-9fd7-d2d24c66e122"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "75398c65-714a-4042-a927-aed8ba5e2126",
      "metadata": {
        "id": "75398c65-714a-4042-a927-aed8ba5e2126"
      },
      "source": [
        "Простые индексы\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ea1e8275-e0c7-4903-8434-6a36678db0b5",
      "metadata": {
        "id": "ea1e8275-e0c7-4903-8434-6a36678db0b5",
        "outputId": "977cb322-f781-4d18-ceff-bf0496b31921"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[ 0  1  2  3]\n",
            " [ 4  5  6  7]\n",
            " [ 8  9 10 11]]\n"
          ]
        }
      ],
      "source": [
        "x = np.arange(12).reshape((3, 4))\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3baeaf39-6fa7-4297-a52a-cb4889cedba0",
      "metadata": {
        "id": "3baeaf39-6fa7-4297-a52a-cb4889cedba0",
        "outputId": "ec387a33-ef32-4430-c1d1-419cf3b34f8d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[ 8  9 10 11]\n"
          ]
        }
      ],
      "source": [
        "print(x[2])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e42bea52-2648-4f4f-8668-9a023323dfa3",
      "metadata": {
        "id": "e42bea52-2648-4f4f-8668-9a023323dfa3",
        "outputId": "78d73d5a-3079-4179-d7c7-1fee909a05b7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[10  8  9]\n"
          ]
        }
      ],
      "source": [
        "print(x[2, [2, 0, 1]])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "47dbc036-743b-43a8-a54d-cd68ab9ad95a",
      "metadata": {
        "id": "47dbc036-743b-43a8-a54d-cd68ab9ad95a",
        "outputId": "b29e3ee5-c9f5-4d40-a185-0a7dab3f36e2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[10  2  6]\n"
          ]
        }
      ],
      "source": [
        "print(x[[2, 0, 1], 2])"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "bd7c98e1-b058-4d00-ab58-e532641b0a51",
      "metadata": {
        "id": "bd7c98e1-b058-4d00-ab58-e532641b0a51"
      },
      "source": [
        "Срезы"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fcf2e86b-9c78-4783-af9f-acd6bb6adc98",
      "metadata": {
        "id": "fcf2e86b-9c78-4783-af9f-acd6bb6adc98",
        "outputId": "84db6e7a-d586-4e0c-ff36-5ff25fe98df0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[ 4  5  6  7]\n",
            " [ 8  9 10 11]]\n"
          ]
        }
      ],
      "source": [
        "print(x[1:])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a8655a06-fe82-4f4f-b7c6-994f67574281",
      "metadata": {
        "id": "a8655a06-fe82-4f4f-b7c6-994f67574281",
        "outputId": "206bd96c-14e1-4ac8-8f3f-23e7635b28e4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[ 6  4  5]\n",
            " [10  8  9]]\n"
          ]
        }
      ],
      "source": [
        "print(x[1:, [2,0,1]])"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "70a72130-ecfa-4bb4-822a-a4dc8be68e83",
      "metadata": {
        "id": "70a72130-ecfa-4bb4-822a-a4dc8be68e83"
      },
      "source": [
        "Маскирование"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0355ca90-94fe-4ae0-a2d8-5d2efee6357b",
      "metadata": {
        "id": "0355ca90-94fe-4ae0-a2d8-5d2efee6357b",
        "outputId": "355fb809-da40-4b74-cca1-e75717a4b2fb"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[ True  True  True False]\n",
            "(4,)\n",
            "(2, 1)\n",
            "[[ 0  1  2]\n",
            " [ 8  9 10]]\n"
          ]
        }
      ],
      "source": [
        "mask = np.array([1,1,1,0], dtype = bool)\n",
        "print(mask)\n",
        "print(mask.shape)\n",
        "row = np.array([0, 2])\n",
        "print(row[:, np.newaxis].shape)\n",
        "print(x[row[:, np.newaxis], mask])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "097c07a6-cd88-4192-99cb-d16f137a47a7",
      "metadata": {
        "id": "097c07a6-cd88-4192-99cb-d16f137a47a7",
        "outputId": "f946fdd0-7511-4123-f9f9-c0161c61b8dd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[ 0  5 10]\n",
            "(4,) (3,)\n",
            "[[ 0  1  2]\n",
            " [ 4  5  6]\n",
            " [ 8  9 10]]\n"
          ]
        }
      ],
      "source": [
        "mask = np.array([1,1,1,0], dtype = bool)\n",
        "row = np.array([0, 1, 2])\n",
        "print(x[row[:], mask])\n",
        "print(mask.shape, row.shape)\n",
        "print(x[row[:, np.newaxis], mask])"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "e8e5f43a-2548-46a7-8477-019537673976",
      "metadata": {
        "id": "e8e5f43a-2548-46a7-8477-019537673976"
      },
      "source": [
        "Использование индексирования"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "1e266d06-2de8-4814-926a-227afdb7e938",
      "metadata": {
        "id": "1e266d06-2de8-4814-926a-227afdb7e938"
      },
      "source": [
        "Генерация на плоскости точек"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e8ff86bb-d13f-4821-9bed-944102497427",
      "metadata": {
        "id": "e8ff86bb-d13f-4821-9bed-944102497427"
      },
      "outputs": [],
      "source": [
        "rng = np.random.default_rng(seed=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d17deea3-9ebd-41b3-be62-f8b9f91411a5",
      "metadata": {
        "id": "d17deea3-9ebd-41b3-be62-f8b9f91411a5",
        "outputId": "def0a4a6-5d18-4bd5-fa66-64afe73e61dd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "(100, 2)\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "x = rng.multivariate_normal([0, 0], [[1, 2], [2, 5]], 100)\n",
        "print(x.shape)\n",
        "plt.scatter(x[:, 0], x[:, 1])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "44532c50-a2ec-451f-82bf-f44e2613e43f",
      "metadata": {
        "id": "44532c50-a2ec-451f-82bf-f44e2613e43f",
        "outputId": "9b31e96f-09aa-4193-85f4-db40cbfc7f72"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[26 86  2 55 75 93 16 73 54 95 53 92 78 13  7 30 22 24 33  8 43 62  3 71\n",
            " 45 48  6 99 82 76]\n"
          ]
        }
      ],
      "source": [
        "np.random.seed(0)\n",
        "inx = np.random.choice(100, 30, replace=False)\n",
        "print(inx)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0803e909-b48f-4f51-bf92-17c8597dd5f7",
      "metadata": {
        "id": "0803e909-b48f-4f51-bf92-17c8597dd5f7",
        "outputId": "e832c007-e843-4190-a728-278cff0e85ab"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<matplotlib.collections.PathCollection at 0x24cea1b7110>"
            ]
          },
          "execution_count": 38,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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mhAPDw+z7+TJkzm+ls/hTQghhBDlgzwJkaCgIHO7EoyAUFAcOHAA3bp1M9tSUlJw/Phx1KlTJ/9nK4QQQogyRZF0zfj7++PBBx/ElClTTJ0HxQc7aMigQYOK4i2FEEIIUQopMh8RCg9XV1fcd999SEhIMMZmf/zxhylaFUIIIYQgThkZGRkl9VKwfZfdMyxcZZRFCCGEECWfvKzfmjUjhBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCCIchISKEEEIIhyEhIoQQQgiHISEihBBCiLInRA4ePIjbbrsNlStXhr+/P7p164bVq1cX1dsJIYQQohRSZELk5ptvRmpqKv744w/8888/aNOmjdl2/vz5onpLIYQQQpQyikSIhIWF4dChQ3jmmWfQunVrNGrUCNOnT0d8fDx2794NR5ORkYHExEQjlIQQQghRxoRIpUqV0KRJE3zxxReIi4szC/7cuXMRHByM9u3b5/i6pKQkREdHZ7kVFidPnsQLL7yA7t27w8/PD15eXnBzc0O9evUwaNAgLF68GCkpKYX2fkIIIYS4Mq4oApycnPD777+jf//+ZtF3dnY2IuSXX35BYGBgjq+bNm0aXnrppUI9l8jISDz55JOYN28efH190a9fP9xyyy2oVq0akpOTsXfvXvz555+44447ULNmTbz//vu49dZbC/UchBBCCGEfpwzmKXIJUy0zZsy47HP27dtnoiEUIYwwPPvssyb68Mknn+CHH37Ali1bjAjIKSLCmwVGRGrVqoWoqChT8JpX/v33X1OXwte/8sorGDFihBEj9ti5cycmT56MFStWYMyYMUaQuLi45Pk9hRBCiPJOdHQ0AgICcrV+50mIhIaGIjw8/LLPqV+/Ptav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",
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "select = x[inx]\n",
        "plt.scatter(x[:, 0], x[:, 1], alpha=0.3)\n",
        "plt.scatter(select[:, 0], select[:, 1], s = 200, facecolor = \"none\", edgecolor = 'black')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d4b6b620-2021-415b-9ee4-dfe35039fd25",
      "metadata": {
        "id": "d4b6b620-2021-415b-9ee4-dfe35039fd25",
        "outputId": "09de59da-7fdd-4c5c-ee79-13c36da2a2ee"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[0 1 2 3 4 5 6 7 8 9]\n",
            "[ 0 90 90  3 90  5  6  7 90  9]\n"
          ]
        }
      ],
      "source": [
        "x = np.arange(10)\n",
        "print(x)\n",
        "inx = np.array([2, 8, 4, 1])\n",
        "\n",
        "x[inx] = 90\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e9a04073-f39a-4eb9-9238-aee66ebcf0af",
      "metadata": {
        "id": "e9a04073-f39a-4eb9-9238-aee66ebcf0af",
        "outputId": "4b38d9e2-a25d-409c-a654-f360332e33f7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[0 1 2 3 4 5 6 7 8 9]\n",
            "[0 2 3 3 5 5 6 7 9 9]\n"
          ]
        }
      ],
      "source": [
        "x = np.arange(10)\n",
        "print(x)\n",
        "x[inx] += 1\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d75c6553-9433-4139-a2a5-81120ee5034d",
      "metadata": {
        "id": "d75c6553-9433-4139-a2a5-81120ee5034d",
        "outputId": "e362c75f-4350-444a-e5ff-56ecdd266de6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[0 1 2 3 4 5 6 7 8 9]\n",
            "[0 2 2 3 5 5 6 7 8 9]\n"
          ]
        }
      ],
      "source": [
        "x = np.arange(10)\n",
        "print(x)\n",
        "inx = np.array([4, 4, 4, 4, 4, 1])\n",
        "\n",
        "x[inx] += 1\n",
        "print(x)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d3aaf187-3ba5-4a71-81f5-6505ff8c728c",
      "metadata": {
        "id": "d3aaf187-3ba5-4a71-81f5-6505ff8c728c",
        "outputId": "222450f2-d30b-4ee4-b2ec-e81b94073a87"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[0 1 2 3 4 5 6 7 8 9]\n",
            "[0 2 2 3 9 5 6 7 8 9]\n"
          ]
        }
      ],
      "source": [
        "x = np.arange(10)\n",
        "print(x)\n",
        "\n",
        "np.add.at(x, inx, 1)\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3f15ca67-edcb-442b-8452-bcf0f80cebda",
      "metadata": {
        "id": "3f15ca67-edcb-442b-8452-bcf0f80cebda"
      },
      "source": [
        "Разбиение данных на интервалы"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "aef5aabb-fe17-480d-8649-1fcc042fcce1",
      "metadata": {
        "id": "aef5aabb-fe17-480d-8649-1fcc042fcce1",
        "outputId": "64081055-df0f-498a-9d6d-1903decead8c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[47 51 75 95  3 14 82 94 24 31]\n"
          ]
        }
      ],
      "source": [
        "rng = np.random.default_rng(seed=1)\n",
        "x = rng.integers(100, size=100)\n",
        "print(x[:10])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2c79890b-c1d3-4cf7-a5eb-8f4314113a2f",
      "metadata": {
        "id": "2c79890b-c1d3-4cf7-a5eb-8f4314113a2f",
        "outputId": "7c9ab8c6-1991-4703-d063-4a3c9326c4e2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]\n"
          ]
        }
      ],
      "source": [
        "bins = np.linspace(0, 100, 11)\n",
        "print(bins)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c489a5c0-fd38-4d0e-a300-04815a291420",
      "metadata": {
        "id": "c489a5c0-fd38-4d0e-a300-04815a291420",
        "outputId": "12c961d6-eac5-4b88-c9cf-a571c356007b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
          ]
        }
      ],
      "source": [
        "counts = np.zeros(11)\n",
        "print(counts)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d9b26aaf-5aa8-4341-aa1c-40064f752aeb",
      "metadata": {
        "id": "d9b26aaf-5aa8-4341-aa1c-40064f752aeb",
        "outputId": "278a9bdd-dfe5-4133-a55e-2f39dfa298a4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[ 5  6  8 10  1  2  9 10  3  4]\n"
          ]
        }
      ],
      "source": [
        "i = np.searchsorted(bins, x)\n",
        "print(i[:10])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "02f2b09f-f73b-4544-9cb8-f5f4f5329c93",
      "metadata": {
        "id": "02f2b09f-f73b-4544-9cb8-f5f4f5329c93",
        "outputId": "9f1fbf03-888a-4b6e-fe91-970ec713bd94"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[ 0.  9.  9. 11.  9. 14. 10.  5. 13. 11.  9.]\n"
          ]
        }
      ],
      "source": [
        "np.add.at(counts, i, 1)\n",
        "print(counts)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3d066809-08c7-489b-b16c-8b794d235c4f",
      "metadata": {
        "id": "3d066809-08c7-489b-b16c-8b794d235c4f",
        "outputId": "29124674-8960-4279-f9f0-f052f6b9b019"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "100.0\n"
          ]
        }
      ],
      "source": [
        "print(sum(counts))"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "087effc8-7f43-4162-ab0e-2936eda4a9b0",
      "metadata": {
        "id": "087effc8-7f43-4162-ab0e-2936eda4a9b0"
      },
      "source": [
        "Сортировка массивов"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "291e7d7b-e36c-4515-b490-218ae3ec6ba8",
      "metadata": {
        "id": "291e7d7b-e36c-4515-b490-218ae3ec6ba8",
        "outputId": "057ec8be-8c88-4f92-85ca-d45580167647"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[1, 2, 3, 3, 4, 5, 5, 6, 6, 23, 64, 78, 1435]\n",
            "[3, 2, 5, 1, 4, 6, 78, 64, 23, 5, 3, 1435, 6]\n"
          ]
        }
      ],
      "source": [
        "a = [3,2,5,1,4,6,78,64,23,5,3,1435,6]\n",
        "print(sorted(a))\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "043977fc-be35-4d75-ba1f-3e9bae0ed2dc",
      "metadata": {
        "id": "043977fc-be35-4d75-ba1f-3e9bae0ed2dc",
        "outputId": "ffd4a534-e92a-409e-c87e-1aa50245801b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[1, 2, 3, 3, 4, 5, 5, 6, 6, 23, 64, 78, 1435]\n"
          ]
        }
      ],
      "source": [
        "a.sort()\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9971805f-833a-4601-b331-13e97a42faac",
      "metadata": {
        "id": "9971805f-833a-4601-b331-13e97a42faac",
        "outputId": "9c86f377-c724-4c93-ee74-81871c491047"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[   3    2    5    1    4    6   78   64   23    5    3 1435    6]\n"
          ]
        }
      ],
      "source": [
        "a = [3,2,5,1,4,6,78,64,23,5,3,1435,6]\n",
        "x = np.array(a)\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0886d0df-e1f2-4d81-b93e-fef952e48d4e",
      "metadata": {
        "id": "0886d0df-e1f2-4d81-b93e-fef952e48d4e",
        "outputId": "19279b65-693a-452d-f985-e8d92fcaf6f3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[   1    2    3    3    4    5    5    6    6   23   64   78 1435]\n",
            "[   3    2    5    1    4    6   78   64   23    5    3 1435    6]\n",
            "[   1    2    3    3    4    5    5    6    6   23   64   78 1435]\n"
          ]
        }
      ],
      "source": [
        "print(np.sort(x))\n",
        "print(x)\n",
        "\n",
        "x.sort()\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "41580be3-7e33-4f46-9a34-72212572f314",
      "metadata": {
        "id": "41580be3-7e33-4f46-9a34-72212572f314",
        "outputId": "47664f3b-3ead-4c1d-e305-5ede52114048"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[   3    2    5    1    4    6   78   64   23    5    3 1435    6]\n",
            "[   1    2    3    3    4    5    5    6    6   23   64   78 1435]\n",
            "[ 3  1  0 10  4  2  9  5 12  8  7  6 11]\n",
            "[   1    2    3    3    4    5    5    6    6   23   64   78 1435]\n"
          ]
        }
      ],
      "source": [
        "x = np.array(a)\n",
        "inx = np.argsort(x)\n",
        "print(x)\n",
        "print(np.sort(x))\n",
        "print(inx)\n",
        "print(x[inx])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b8cd41fb-5524-48ed-b06d-c242c4c54f65",
      "metadata": {
        "id": "b8cd41fb-5524-48ed-b06d-c242c4c54f65",
        "outputId": "556c9170-6265-41dd-e3ce-ce4fb818a098"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[4 5 7 9 0 1]\n",
            " [8 9 2 3 8 4]\n",
            " [2 8 2 4 6 5]\n",
            " [0 0 8 7 8 5]]\n",
            "[[0 1 4 5 7 9]\n",
            " [2 3 4 8 8 9]\n",
            " [2 2 4 5 6 8]\n",
            " [0 0 5 7 8 8]]\n",
            "[[0 0 2 3 0 1]\n",
            " [2 5 2 4 6 4]\n",
            " [4 8 7 7 8 5]\n",
            " [8 9 8 9 8 5]]\n"
          ]
        }
      ],
      "source": [
        "rng = np.random.default_rng(seed=1)\n",
        "x = rng.integers(0, 10, size=(4, 6))\n",
        "print(x)\n",
        "\n",
        "print(np.sort(x, axis=1))\n",
        "print(np.sort(x, axis=0))"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "84ec3b15-4bbb-4d90-8655-8a3bd7e74e10",
      "metadata": {
        "id": "84ec3b15-4bbb-4d90-8655-8a3bd7e74e10"
      },
      "source": [
        "Cтруктурированные массивы"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "8651e67b-4126-4bbb-b357-7f2812ef0dc5",
      "metadata": {
        "id": "8651e67b-4126-4bbb-b357-7f2812ef0dc5"
      },
      "source": [
        "Массивы записей"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "99ca1206-e993-4457-83ea-4b1f6bcdbd88",
      "metadata": {
        "id": "99ca1206-e993-4457-83ea-4b1f6bcdbd88",
        "outputId": "8a14f125-f25a-41c0-b023-7a1e82398eb9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Виталий 17 57\n"
          ]
        }
      ],
      "source": [
        "name = ['Ирина', 'Виталий', 'Олег', 'Саша']\n",
        "age = [25, 17, 52, 44]\n",
        "weight = [55.0, 57, 78, 72]\n",
        "\n",
        "i = 1\n",
        "print(name[i], age[i], weight[i])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9f021f75-de92-4e11-bd84-13652e095893",
      "metadata": {
        "id": "9f021f75-de92-4e11-bd84-13652e095893",
        "outputId": "357ef38f-5e7d-4c51-a0c9-9d4b1fd62d02"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[('name_', '<U10'), ('age_', '<i4'), ('weight_', '<f8')]\n"
          ]
        }
      ],
      "source": [
        "data = np.zeros(\n",
        "    4,\n",
        "    dtype = {\n",
        "        \"names\": (\"name_\", \"age_\", \"weight_\"),\n",
        "        \"formats\": (\"U10\", \"i4\", \"f8\")\n",
        "    })\n",
        "\n",
        "print(data.dtype)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d0542103-deb0-40b7-a467-8c27e951eb44",
      "metadata": {
        "id": "d0542103-deb0-40b7-a467-8c27e951eb44",
        "outputId": "84843463-37e6-4755-9d21-ecf5061e4f01"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[('Ирина', 25, 55.) ('Виталий', 17, 57.) ('Олег', 52, 78.)\n",
            " ('Саша', 44, 72.)]\n"
          ]
        }
      ],
      "source": [
        "data[\"name_\"] = name\n",
        "data[\"age_\"] = age\n",
        "data[\"weight_\"] = weight\n",
        "\n",
        "print(data)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9a47b93b-d367-4990-b881-347a6facf167",
      "metadata": {
        "id": "9a47b93b-d367-4990-b881-347a6facf167",
        "outputId": "99f92b82-f9cc-4c5a-cbb4-7555c8c6e207"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['Ирина' 'Виталий' 'Олег' 'Саша']\n"
          ]
        }
      ],
      "source": [
        "print(data[\"name_\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "dadd2ff3-efd8-4820-8d9f-932e1a85f691",
      "metadata": {
        "id": "dadd2ff3-efd8-4820-8d9f-932e1a85f691",
        "outputId": "5c873fe4-19a8-460c-f661-8c3a52432417"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "('Ирина', 25, 55.0)\n"
          ]
        }
      ],
      "source": [
        "print(data[0])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "41433c46-494f-4305-a7f1-7a195972f800",
      "metadata": {
        "id": "41433c46-494f-4305-a7f1-7a195972f800",
        "outputId": "8ca571be-4572-421e-ead1-63a4184a4317"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Саша\n"
          ]
        }
      ],
      "source": [
        "print(data[-1][\"name_\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "5cf76a75-8482-4613-ae38-e234ad017d56",
      "metadata": {
        "id": "5cf76a75-8482-4613-ae38-e234ad017d56",
        "outputId": "12a98a2f-14c8-4304-d61b-9cda8c72c3e6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[('Ирина', 25, 55.) ('Виталий', 17, 57.) ('Олег', 52, 78.)\n",
            " ('Саша', 44, 72.)]\n"
          ]
        }
      ],
      "source": [
        "data_rec = data.view(np.recarray)\n",
        "print(data_rec)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "20f324d2-bd4f-4a61-a8b7-cc1cca0f0cd8",
      "metadata": {
        "id": "20f324d2-bd4f-4a61-a8b7-cc1cca0f0cd8",
        "outputId": "9985e9f8-2c83-4b61-d021-9cd04ac0dc01"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['Ирина' 'Виталий' 'Олег' 'Саша']\n",
            "Саша\n"
          ]
        }
      ],
      "source": [
        "print(data_rec.name_)\n",
        "print(data_rec[-1].name_)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "205ec684-a0c4-4038-b4ca-82d70890dba3",
      "metadata": {
        "id": "205ec684-a0c4-4038-b4ca-82d70890dba3",
        "outputId": "adf2258f-9f07-4e90-fee3-2ac55dec75d8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[ True  True False False]\n"
          ]
        }
      ],
      "source": [
        "print(data[\"age_\"] < 30)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "44a426de-efa8-4685-9706-3873626a0157",
      "metadata": {
        "id": "44a426de-efa8-4685-9706-3873626a0157",
        "outputId": "340e76e6-060d-4dae-90d4-4f9c88f75dca"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[('Ирина', 25, 55.) ('Виталий', 17, 57.)]\n"
          ]
        }
      ],
      "source": [
        "print(data[data[\"age_\"] < 30])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fe4f71dd-4706-42b8-b487-846e4fd1a419",
      "metadata": {
        "id": "fe4f71dd-4706-42b8-b487-846e4fd1a419",
        "outputId": "57c97714-d1a4-4442-a536-9d0c976f13c1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['Ирина' 'Виталий']\n"
          ]
        }
      ],
      "source": [
        "print(data[data[\"age_\"] < 30][\"name_\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "34c499bb-36f4-48cb-9cd0-36f626f6b7d1",
      "metadata": {
        "id": "34c499bb-36f4-48cb-9cd0-36f626f6b7d1",
        "outputId": "c694e639-034b-4540-96f4-9e4a051e2ccc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[(0, [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])\n",
            " (0, [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])]\n"
          ]
        }
      ],
      "source": [
        "tp = np.dtype([(\"id\", \"i8\"), (\"mat\", \"f8\", (3, 3))])\n",
        "x = np.zeros(2, dtype=tp)\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ba5b8150-95af-4a6b-8906-87ab17b61c9f",
      "metadata": {
        "id": "ba5b8150-95af-4a6b-8906-87ab17b61c9f",
        "outputId": "6ac8bbdd-54cd-4c34-e71e-f5f780b32c3d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[(0, [[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])\n",
            " (0, [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])]\n"
          ]
        }
      ],
      "source": [
        "x[\"mat\"][0] = np.array([[1,2,3], [4,5,6],[7,8,9]])\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9f7d89d6-2220-445a-af64-e747287e602b",
      "metadata": {
        "id": "9f7d89d6-2220-445a-af64-e747287e602b"
      },
      "outputs": [],
      "source": [
        "data = [('Ирина', 25, 55), (\"Виталий\", 17, 57)]\n",
        "\n",
        "name = ['Ирина', 'Виталий', 'Олег', 'Саша']\n",
        "age = [25, 17, 52, 44]\n",
        "weight = [55.0, 57, 78, 72]\n",
        "\n",
        "dtype = {\"names\": (\"name_\", \"age_\", \"weight_\"), \"formats\": (\"U10\", \"i4\", \"f8\")}\n",
        "\n",
        "data_rec = np.rec.array(datam dtype = dtype)"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.13.5"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}