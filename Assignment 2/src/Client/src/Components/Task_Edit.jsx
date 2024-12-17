import React from "react";

function Task_Edit({ editTask, setEditTask, updateTask }) {
    return (
        <div className="bg-gray-900 bg-opacity-50 fixed top-0 left-0 w-full h-full flex justify-center items-center ">
            <div className="mt-6 bg-gray-50 p-4 rounded-md shadow-md max-w-[500px] ">
                <h2 className="text-lg font-bold mb-4">Edit Task</h2>
                <form onSubmit={updateTask}>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-gray-600">Title</label>
                            <input
                                type="text"
                                name="title"
                                value={editTask.title || ""}
                                onChange={(e) =>
                                    setEditTask({
                                        ...editTask,
                                        title: e.target.value,
                                    })
                                }
                                className="border-gray-300 border rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-gray-600">
                                Due Date
                            </label>
                            <input
                                type="date"
                                name="due_date"
                                value={editTask.due_date || ""}
                                onChange={(e) =>
                                    setEditTask({
                                        ...editTask,
                                        due_date: e.target.value,
                                    })
                                }
                                className="border-gray-300 border rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-gray-600">
                                Description
                            </label>
                            <textarea
                                name="description"
                                value={editTask.description || ""}
                                onChange={(e) =>
                                    setEditTask({
                                        ...editTask,
                                        description: e.target.value,
                                    })
                                }
                                className="border-gray-300 border rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
                            ></textarea>
                        </div>
                    </div>
                    <div className="mt-4 space-x-2">
                        <button
                            type="submit"
                            className="bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600"
                        >
                            Save Changes
                        </button>
                        <button
                            type="button"
                            onClick={() => setEditTask(null)} // Cancel edit
                            className="bg-gray-500 text-white py-2 px-4 rounded-md hover:bg-gray-600"
                        >
                            Cancel
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Task_Edit;
