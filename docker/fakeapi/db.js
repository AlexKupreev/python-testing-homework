// @ts-check
/**
* Runs fake server with fake data.
*
* @typedef { object } spec - Specification for fake API.
* @property { CustomProperty[] } customproperties
*
* @returns { spec } - Routes spec for json-server.
*
* @see https://www.npmjs.com/package/json-server
*/
// @ts-check
/**
* Fake data generation for testing.
*
* @typedef { import(
* "../../src/services/types"
* ).CustomProperty } CustomProperty
*/
/**
* @type { CustomProperty[] }
*/
const photos = [{
  'id': '1',
  'url': 'https://picture.example.com/oitwroihfgiawe.jpg',
}, {
  'id': '2',
  'url': 'https://picture.example.com/34fdroihfgksde.jpg',
}, {
  'id': '3',
  'url': 'https://picture.example.com/lbio34986trtwg.jpg',
}]

function prepareTestData() {
  return {
    photos,
  }
}
module.exports = prepareTestData
