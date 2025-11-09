# Note: This project was inspired by a Real Python tutorial on FastAPI.
# I modified and expanded parts of the original example to explore CRUD operations and API design patterns.
# This repository is for educational purposes only.

from fastapi import FastAPI, HTTPException # for creating API and handling exceptions
from mongita import MongitaClientDisk # using Mongita as a lightweight database (files instead of server)
from pydantic import BaseModel # for data validation and settings management / more complex objects

# Creating a subclass called Shape from pydantic's BaseModel to define the structure of a Shape object
class Shape(BaseModel):
    name: str # name of the shape
    no_of_sides: int # number of sides of the shape
    id: int # unique identifier for the shape


# Creating an instance of FastAPI
app = FastAPI()

# Setting up the Mongita database and collection
client = MongitaClientDisk()
db = client.db
shapes = db.shapes

# GET endpoint for the root URL
@app.get("/") # Decorator to define a GET endpoint at the root URL
async def root():
    return {"message": "Hello, World!"}

# GET endpoint to retrieve all shapes
@app.get("/shapes") # Decorator to define a GET endpoint at /shapes within the overall dictionary
async def get_shapes():
    existing_shapes = shapes.find({})
    return [
        {key: shape[key] for key in shape if key != '_id'}
        for shape in existing_shapes
    ]

# GET endpoint to retrieve a specific shape by its ID
@app.get("/shapes/{shape_id}") # Decorator to define a GET endpoint at /shapes/{shape_id} where shape_id is a path parameter
async def get_shapes(shape_id: int):
    # Check if a shape with the given ID exists
    if shapes.count_documents({'id': shape_id}) > 0:
        shape = shapes.find_one({'id': shape_id})
        return {key: shape[key] for key in shape if key != '_id'}
    
    raise HTTPException(status_code=404, detail=f'No shape with id {shape_id} found') # raise 404 if shape not found

# POST endpoint to add a new shape
@app.post("/shapes") # Decorator to define a POST endpoint at /shapes in the overall dictionary
async def post_shape(shape: Shape):
    shapes.insert_one(shape.model_dump()) # insert the new shape into the database
    return shape

# PUT endpoint to update an existing shape by its ID
@app.put('/shapes/{shape_id}') # Decorator to define a PUT endpoint at /shapes/{shape_id} where shape_id is a path parameter
async def update_shape(shape_id: int, shape: Shape):
    # Check if a shape with the given ID exists
    if shapes.count_documents({'id': shape_id}) > 0:
        shapes.replace_one({'id': shape_id}, shape.model_dump(), upsert=True)
        return shape
    raise HTTPException(status_code=404, detail=f'No shape with id {shape_id} found') # raise 404 if shape to update does not exist

# DELETE endpoint to remove a shape by its ID
@app.delete('/shapes/{shape_id}') # Decorator to define a DELETE endpoint at /shapes/{shape_id} where shape_id is a path parameter
async def delete_shape(shape_id: int):
    deleted_result = shapes.delete_one({'id': shape_id})
    # Check if any shape was deleted
    if deleted_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f'No shape with id {shape_id} found') # raise 404 if no shape was deleted
    return {'message': f'Shape with id {shape_id} deleted successfully'} # return a success message