import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import './plugins/axios';
import devtools from '@vue/devtools'

import './assets/main.css';

const app = createApp(App);
''
devtools.connect('http://localhost', '3000')
app.use(createPinia());
app.use(router);

app.mount('#app');
