export const updateObject = (oldObject, updatedProperties) => {
  return{
    ...oldObject, // Updates the old object.
    ...updatedProperties
  }
}
