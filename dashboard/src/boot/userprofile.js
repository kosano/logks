import { LocalStorage } from 'quasar'

export class UserProfile {
    static setLocalUserProfile(profile) {
        LocalStorage.set('user', profile)
    }
    static getLocalUserProfile() {
        return LocalStorage.getItem('user')
    }
}

