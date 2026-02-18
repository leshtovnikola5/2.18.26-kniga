if "books" not in st.session_state:
    st.session_state.books = []

title = st.text_input("Заглавие")
author = st.text_input("Автор")

if st.button("Добави книга"):
    book = {
        "title": title,
        "author": author
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

st.write("### Списък с книги:")
st.write(st.session_state.books)
