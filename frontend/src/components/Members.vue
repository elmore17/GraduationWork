<template>
    <Nav/>
    <div class="relative overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-900 uppercase dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-6 py-3">
                        ФИО
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in usersecz" class="bg-white dark:bg-gray-800">
                    <th :key="user.id" scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        {{ user.user_name }}
                    </th>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
import Nav from './Nav.vue';
export default{
    name: 'Members',
    components:{
        Nav,
    },
    data(){
        return {
            usersecz: [],
        };
    },
    mounted(){
        this.checkuserecz();
    },
    methods:{
        async checkuserecz(){
            try{
                const getresponse = await axios.get('http://127.0.0.1:83/getusers')
                this.usersecz = getresponse.data.users;
            }
            catch(error){
                console.log(error)
            }
        },
    },
};
</script>