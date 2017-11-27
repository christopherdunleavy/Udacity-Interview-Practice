def question1(main, sub):
	if (len(sub) > len(main)):
		return False

	main = main.lower()
	sub = sub.lower()

	main_list = list(main)
	sub_list = list(sub)

	for s in main_list:
		if s in sub_list:
			sub_list.pop(sub_list.index(s))
			if len(sub_list) == 0:
				return True
		else:
			sub_list = list(sub)

	return False


def main():
    print question1("uda#$city", "$c#")

if __name__ == "__main__":
    main()