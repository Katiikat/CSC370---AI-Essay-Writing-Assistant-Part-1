# To use the website, duh
import wikipedia
import PySimpleGUI


# Welcome the users to improve user experience
def intro():
    intro = "\n\nWelcome to my very first AI!\nThis Wiki Researching AI is quite simple to use.\n\n" \
            "Simply enter in something you would like to research on Wikipedia.\n" \
            "Press Enter and the AI will display that contents of the page you are researching." \
            "\nHow cool is that!"

    print(intro)
    add_to_file(intro)

    question_readiness = "\n\nAre you ready to get started? Type Y or N."
    add_to_file(question_readiness + "\n")

    ready_ans = input(question_readiness)
    add_to_file(ready_ans + "\n")
    ready_ans = ready_ans.upper()

    if ready_ans == "Y" or ready_ans == "YES":
        return True
    else:
        double_check_readiness = "\n\nAre you sure you want to exit? Type Y or N."

        double_check_ans = input(double_check_readiness)
        double_check_ans.upper()

        if double_check_ans == "Y" or double_check_ans == "YES":
            return False
        elif double_check_ans == "N" or double_check_ans == "NO":
            return True
        else:
            print("\n\nNo viable answer could be found.\nTry again later.")
            return False


def create_essay(research_topic):
    # Create a variable to hold the wiki page info
    research_page = wikipedia.page(research_topic, auto_suggest=False)

    # display the page to the screen
    print(f"\n\n\t\t*** {research_topic.upper()} ***")
    print("_" * 50)

    print("\n\t\t*** Content ***\n")
    print(research_page.content.replace("== References ==", " "))
    print("_" * 50)

    print("\n\t\t*** References ***\n")
    raw_references = research_page.references
    for each_ref in raw_references:
        print(each_ref)
    # print(research_page.references)
    print("_" * 50)


def add_to_file(string_to_add):
    # raw_file = open("Research Raw Data.txt", "wb")

    try:
        raw_file = open("Research Raw Data.txt", "a+")  # "a+", for appending to a file
    except IOError:
        print("Could not open file!")
    with raw_file:
        print("Time to write to a file!")
        raw_file.write(string_to_add)


def main():
    proceed = intro()

    if proceed:
        print("\n\n", "_" * 50, "\n")
        what_to_research_question = "\t\tWhat would you like to research?\n\t\tTopic: "
        research_topic = input(what_to_research_question)
        create_essay(research_topic)
    else:
        exit()


if __name__ == '__main__':
    main()
