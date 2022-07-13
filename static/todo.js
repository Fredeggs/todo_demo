$(".delete-todo").click(deleteTodo);

async function deleteTodo() {
  const ID = $(this).data("id");
  await axios.delete(`/api/todos/${ID}`);
  $(this).parent().remove();
}
