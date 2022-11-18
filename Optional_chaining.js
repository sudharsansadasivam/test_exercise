const house = {
  price: 1000000,
  currency: 'USD',
  address: {
    city: 'New York',
    street: 'Main street',
    postal_code: '1234 AB',
    state: {
      name: 'New York',
      abbreviation: 'N.Y.'
    }
  },
  owner: null
}

const state = house.address && house.address.state ? house.address.state.name : null

#Chaining Operator
const city = house?.address?.city // "New York"
const nonExisting = house?.roof?.material // Undefined
const houseNumber = house?.address?.number // Undefined
const state = house?.address?.state?.abbreviation // "N.Y."
