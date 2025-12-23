import heapq

def min_cost(cable_len):
    if not cable_len:
        return 0
    
    heap = list(cable_len)

    heapq.heapify(heap)
    total_cost = 0
    step = 1

    print(f"Початкова купа: {heap}")

    # Поки в купі більше одного елемента
    while len(heap) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        # Об'єднуємо їх і додаємо витрати
        cost = first + second
        total_cost += cost

        # Повертаємо об'єднаний кабель назад у купу
        heapq.heappush(heap, cost)

        # Покроковий вивід
        print(f"\nКрок {step}:")
        print(f"  Дістаємо: {first} і {second}")
        print(f"  Вартість з'єднання: {cost}")
        print(f"  Накопичені витрати: {total_cost}")
        print(f"  Купа після вставки {cost}: {heap}")
        step += 1

    print(f"\nЗагальні мінімальні витрати: {total_cost}")
    return total_cost


# Приклад використання
cables = [4, 2, 3, 6, 8, 12]
min_cost(cables)

