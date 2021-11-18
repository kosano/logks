
import axios from 'axios'
import { UserProfile } from './userprofile'

var headers = { 'Content-type': 'application/json' }

// if (!!UserProfile.getLocalUserProfile()) {
//     headers['Authorization'] = `Bearer ${UserProfile.getLocalUserProfile()['token']}`
// }

const api = axios.create({ baseURL: 'http://localhost:8081', headers: headers })

export { axios, api }