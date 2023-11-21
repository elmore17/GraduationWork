<script>
import axios from 'axios';

export default{
    name: 'Authorize',
    data(){
        return {
            username: '',
            password: '',
        };
    },
    methods:{
        loginUser(){
            const data = {
                username: this.username,
                password: this.password,
            };
            axios.post('http://127.0.0.1:83/login',data)
                .then(response => {
                    if (response.data.message == "Successfully"){
                        window.location.href = '/main';
                    }else{
                        console.log("Error");
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
};
</script>


<template>
    <div class="container mx-auto grid justify-items-center mt-40" id="example-1">
        <form  @submit.prevent = "Authorize" class="grid justify-items-center border-2 decoration-sky-500/100 max-w-md h-96 rounded-3xl">
            <img src="../assets/logo.svg" alt="logo" class="pt-3 w-24 h-24">
            <p class="pt-3">Авторизация</p>
            <p class="pt-3">Username</p>
            <input v-model="username" type="name" placeholder="username" class="pl-3 pr-3 border-2 decoration-sky-500/100 w-96 rounded-3xl ml-2 mr-2">
            <p class="pt-3">Password</p>
            <input v-model="password" type="password" placeholder="password" class="pl-3 pr-3 border-2 decoration-sky-500/100 w-96 rounded-3xl ml-2 mr-2">
            <a href="#" class="text-blue-400">нет аккаунта?</a>
            <button class="mt-3 mb-3 w-52 bg-blue-700 hover:bg-blue-600 rounded-3xl text-white h-12" type="submit" @click="loginUser()">Войти</button>
        </form>
    </div>
</template>