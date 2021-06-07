def cut(filename, delimiter, field):
    with open(filename, "r") as file:
        result = ""
        lines = file.readlines()

        for line in lines:
            line = line.split(delimiter)

            if type(field) == int:
                result += line[field - 1]

                result = result[: -1]

            else:
                for element in field:
                    result += line[element - 1] + delimiter

                result = result[: -1]

            result += "\n"

    return result[: -1]
