def perform_operations_1_to_30(my_list):
    while True:
        print("\nOperations 1-30 Menu:")
        print("1. Append")
        print("2. Extend")
        print("3. Insert")
        print("4. Remove")
        print("5. Pop")
        print("6. Clear")
        print("7. Index")
        print("8. Count")
        print("9. Sort")
        print("10. Reverse")
        print("11. Copy")
        print("12. List Comprehension")
        print("13. Membership Test (in)")
        print("14. Length (len)")
        print("15. Maximum (max)")
        print("16. Minimum (min)")
        print("17. Sum (sum)")
        print("18. Slicing")
        print("19. Range Slicing")
        print("20. Concatenation (+)")
        print("21. Repetition (*)")
        print("22. List Membership Test (in)")
        print("23. Iteration (for)")
        print("24. Any (any)")
        print("25. All (all)")
        print("26. Filter")
        print("27. Map")
        print("28. Reduce")
        print("29. Zip")
        print("30. Enumerate")
        print("0. Exit")

        choice = int(input("Enter your choice (1-30, 0 to exit): "))

        if choice == 0:
            break
        elif choice == 1:
            element = int(input("Enter the element to append: "))
            my_list.append(element)
        elif choice == 2:
            other_list = list(map(int, input("Enter elements to extend (space-separated): ").split()))
            my_list.extend(other_list)
        elif choice == 3:
            index = int(input("Enter the index to insert at: "))
            element = input("Enter the element to insert: ")
            my_list.insert(index, element)
        elif choice == 4:
            element = int(input("Enter the element to remove: "))
            my_list.remove(element)
        elif choice == 5:
            index = int(input("Enter the index to pop (default is the last element): "))
            popped_element = my_list.pop(index)
            print("Popped element:", popped_element)
        elif choice == 6:
            my_list.clear()
        elif choice == 7:
            element = int(input("Enter the element to find index: "))
            try:
                index = my_list.index(element)
                print("Index of", element, "is", index)
            except ValueError:
                print(element, "not found in the list.")
        elif choice == 8:
            element = int(input("Enter the element to count: "))
            count = my_list.count(element)
            print("Count of", element, "is", count)
        elif choice == 9:
            my_list.sort()
        elif choice == 10:
            my_list.reverse()
        elif choice == 11:
            new_list = my_list.copy()
            print("Shallow copy created:", new_list)
        elif choice == 12:
            n = int(input("Enter the number of elements for list comprehension: "))
            squared_list = [i ** 2 for i in range(n)]
            print("List comprehension result:", squared_list)
        elif choice == 13:
            element = int(input("Enter the element to check membership: "))
            print(element, "is", "in" if element in my_list else "not in", "the list.")
        elif choice == 14:
            length = len(my_list)
            print("Length of the list:", length)
        elif choice == 15:
            maximum = max(my_list)
            print("Maximum element in the list:", maximum)
        elif choice == 16:
            minimum = min(my_list)
            print("Minimum element in the list:", minimum)
        elif choice == 17:
            total_sum = sum(my_list)
            print("Sum of elements in the list:", total_sum)
        elif choice == 18:
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            sliced_list = my_list[start:end]
            print("Sliced list:", sliced_list)
        elif choice == 19:
            start = int(input("Enter the start index for range slicing: "))
            end = int(input("Enter the end index for range slicing: "))
            step = int(input("Enter the step size for range slicing: "))
            range_sliced_list = my_list[start:end:step]
            print("Range sliced list:", range_sliced_list)
        elif choice == 20:
            other_list = list(map(int, input("Enter elements for concatenation (space-separated): ").split()))
            concatenated_list = my_list + other_list
            print("Concatenated list:", concatenated_list)
        elif choice == 21:
            repetition_factor = int(input("Enter the repetition factor: "))
            repeated_list = my_list * repetition_factor
            print("Repeated list:", repeated_list)
        elif choice == 22:
            sublist = list(map(int, input("Enter elements for sublist to check membership (space-separated): ").split()))
            print("Sublist is", "in" if sublist in my_list else "not in", "the list.")
        elif choice == 23:
            print("Iterating over the list:")
            for element in my_list:
                print(element, end=" ")
            print()
        elif choice == 24:
            any_result = any(my_list)
            print("Any result (True if at least one element is True):", any_result)
        elif choice == 25:
            all_result = all(my_list)
            print("All result (True if all elements are True):", all_result)
        elif choice == 26:
            # Implement filter operation

            pass
        elif choice == 27:
            # Implement map operation



            pass
        elif choice == 28:
            # Implement reduce operation
            pass
        elif choice == 29:
            # Implement zip operation
            pass
        elif choice == 30:
            # Implement enumerate operation
            pass
        else:
            print("Invalid choice. Please enter a valid option.")

def perform_operations_31_to_60(my_list):
    while True:
        print("\nOperations 31-60 Menu:")
        print("31. List to Set Conversion")
        print("32. List to Tuple Conversion")
        print("33. List to String Conversion")
        print("34. List Concatenation (+)")
        print("35. List Clear")
        print("36. List Comparison")
        print("37. List Deletion")
        print("38. List Extend (+=)")
        print("39. List Insert")
        print("40. List Pop")
        print("41. List Remove")
        print("42. List Reverse")
        print("43. List Sort (sorted())")
        print("44. List Slicing with Steps")
        print("45. List Comprehension with Condition")
        print("46. List Extend Using Asterisk (*)")
        print("47. List Copy")
        print("48. List Count Using Count Method")
        print("49. List Concatenation Using Extend Method")
        print("50. List Max Using Max Function")
        print("51. List Min Using Min Function")
        print("52. List Sum Using Sum Function")
        print("53. List Sort Using Sorted Function")
        print("54. List Reverse Using Reversed Function")
        print("55. List Clear Using Clear Method")
        print("56. List Nested")
        print("57. List Initialization")
        print("58. List In-Place Changes")
        print("59. List Comparison Using Comparison Operators")
        print("60. List Equality")
        print("0. Exit")

        choice = int(input("Enter your choice (31-60, 0 to exit): "))

        if choice == 0:
            break
        elif choice == 31:
            set_conversion = set(my_list)
            print("List converted to set:", set_conversion)
        elif choice == 32:
            tuple_conversion = tuple(my_list)
            print("List converted to tuple:", tuple_conversion)
        elif choice == 33:
            string_conversion = ''.join(map(str, my_list))
            print("List converted to string:", string_conversion)
        elif choice == 34:
            other_list = list(map(int, input("Enter elements for concatenation (space-separated): ").split()))
            my_list += other_list
            print("Concatenated list:", my_list)
        elif choice == 35:
            my_list.clear()
        elif choice == 36:
            other_list = list(map(int, input("Enter elements for comparison (space-separated): ").split()))
            comparison_result = my_list == other_list
            print("List comparison result:", comparison_result)
        elif choice == 37:
            index = int(input("Enter the index to delete: "))
            del my_list[index]
            print("Element at index", index, "deleted.")
        elif choice == 38:
            other_list = list(map(int, input("Enter elements to extend (space-separated): ").split()))
            my_list.extend(other_list)
            print("Extended list:", my_list)
        elif choice == 39:
            index = int(input("Enter the index to insert at: "))
            element = int(input("Enter the element to insert: "))
            my_list.insert(index, element)
            print("List after insertion:", my_list)
        elif choice == 40:
            index = int(input("Enter the index to pop (default is the last element): "))
            popped_element = my_list.pop(index)
            print("Popped element:", popped_element)
        elif choice == 41:
            element = int(input("Enter the element to remove: "))
            my_list.remove(element)
            print("List after removal:", my_list)
        elif choice == 42:
            my_list.reverse()
            print("Reversed list:", my_list)
        elif choice == 43:
            sorted_list = sorted(my_list)
            print("Sorted list:", sorted_list)
        elif choice == 44:
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            step = int(input("Enter the step size for slicing: "))
            sliced_list = my_list[start:end:step]
            print("Sliced list with steps:", sliced_list)
        elif choice == 45:
            condition = int(input("Enter the condition for list comprehension: "))
            filtered_list = [i for i in my_list if i > condition]
            print("Filtered list:", filtered_list)
        elif choice == 46:
            repetition_factor = int(input("Enter the repetition factor: "))
            repeated_list = my_list * repetition_factor
            print("Repeated list:", repeated_list)
        elif choice == 47:
            copy_list = my_list.copy()
            print("Shallow copy created:", copy_list)
        elif choice == 48:
            element = int(input("Enter the element to count: "))
            count = my_list.count(element)
            print("Count of", element, "is", count)
        elif choice == 49:
            other_list = list(map(int, input("Enter elements for concatenation (space-separated): ").split()))
            my_list.extend(other_list)
            print("Concatenated list using extend method:", my_list)
        elif choice == 50:
            maximum = max(my_list)
            print("Maximum element in the list:", maximum)
        elif choice == 51:
            minimum = min(my_list)
            print("Minimum element in the list:", minimum)
        elif choice == 52:
            total_sum = sum(my_list)
            print("Sum of elements in the list:", total_sum)
        elif choice == 53:
            sorted_list = sorted(my_list)
            print("Sorted list using sorted function:", sorted_list)
        elif choice == 54:
            reversed_list = list(reversed(my_list))
            print("Reversed list using reversed function:", reversed_list)
        elif choice == 55:
            my_list.clear()
            print("List cleared.")
        elif choice == 56:
            nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print("Nested list:", nested_list)
        elif choice == 57:
            n = int(input("Enter the number of elements for list initialization: "))
            initialized_list = [int(input("Enter element: ")) for _ in range(n)]
            print("Initialized list:", initialized_list)
        elif choice == 58:
            my_list[0] = 100  # In-place change, modifying the first element
            print("List after in-place change:", my_list)
        elif choice == 59:
            other_list = list(map(int, input("Enter elements for comparison (space-separated): ").split()))
            comparison_result = my_list > other_list
            print("List comparison result using comparison operators:", comparison_result)
        elif choice == 60:
            other_list = list(map(int, input("Enter elements for equality check (space-separated): ").split()))
            equality_result = my_list == other_list
            print("List equality result:", equality_result)
        else:
            print("Invalid choice. Please enter a valid option.")

def main2():
    my_list = [1, 2, 3, 4, 5]

    while True:
        print("\nMain Menu:")
        print("1. Perform Operations 1-30")
        print("2. Perform Operations 31-60")
        print("0. Exit")

        main_choice = int(input("Enter your choice (0-2): "))

        if main_choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif main_choice == 1:
            perform_operations_1_to_30(my_list)
        elif main_choice == 2:
            perform_operations_31_to_60(my_list)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main2()
