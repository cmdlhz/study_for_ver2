import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize Firebase
var config = {

};
firebase.initializeApp(config);
const db = firebase.firestore();

db.settings({ timestampsInSnapshots: true});

export default db;