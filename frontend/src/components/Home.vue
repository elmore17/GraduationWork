<template>
    <Nav />
    <div class="flex items-center justify-center mb-4">
        <h5>Загрузите протокол защиты ВКР</h5>
    </div>
    <div class="flex items-center justify-center">
        <label for="dropzone-file" class="flex flex-col items-center justify-center w-50 h-50 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
            <div class="flex flex-col items-center justify-center pt-5 pb-6">
                <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                </svg>
                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                <p class="text-xs text-gray-500 dark:text-gray-400">DOCX</p>
            </div>
            <input id="dropzone-file" type="file" class="hidden" @change="handleFileUpload" />
        </label>
    </div>
    <div class="flex space-around flex-start">
        <div class="w-full">
            <div class="max-w-screen-xl flex flex-wrap items-baseline mx-auto p-4 mt-5">
                <h5 class="mb-4 mr-4">Выберете дату</h5>
                <div class="relative max-w-sm">
                    <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                        <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                        </svg>
                    </div>
                    <input ref="datepicker1" datepicker type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Выберете дату">
                </div>
            </div>
            <div class="max-w-screen-xl flex flex-wrap items-baseline mx-auto p-4 mt-5">
                <h5 class="mb-4 mr-4">Председатель Государственной экзаменационной комиссии</h5>
                <div class="relative max-w-sm">
                    <input v-model="namegospred" type="text" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="ФИО" required>
                </div>
            </div>
            <div class="max-w-screen-xl flex flex-wrap items-baseline mx-auto p-4 mt-5">
                <h5 class="mb-4 mr-4">Члены Государственной экзаменационной комиссии (фамилия и инициалы)</h5>
                <div class="relative max-w-sm">
                    <button data-modal-target="default-modal" data-modal-toggle="default-modal" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
                    Просмотр
                    </button>
                    <div id="default-modal" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
                        <div class="relative p-4 w-full max-w-2xl max-h-full">
                            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                                        Просмотр членов Государственной экзаменационной комиссии
                                    </h3>
                                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="default-modal">
                                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                                        </svg>
                                        <span class="sr-only">Close modal</span>
                                    </button>
                                </div>
                                <div class="p-4 md:p-5 space-y-4">
                                    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                                <tr>
                                                    <th scope="col" class="px-6 py-3">
                                                        ФИО
                                                    </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                                        Apple MacBook Pro 17"
                                                    </th>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                                    <button data-modal-hide="default-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Принять</button>
                                    <button data-modal-hide="default-modal" type="button" class="ms-3 text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Отмена</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="selectedUser">
                <div class="max-w-screen-xl flex flex-wrap items-baseline mx-auto p-4 mt-5">
                    <h5 class="mb-4 mr-4">Оценка за ВКР</h5>
                    <div class="relative max-w-sm">
                        <select id="score" v-model="selectedUser.score" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" @change="ScoresPush(selectedUser)">
                            <option disabled>Выберете оценку</option>
                            <option value="otl">отлично</option>
                            <option value="hor">хорошо</option>
                            <option value="udov">удовлетворительно</option>
                        </select>
                    </div>
                </div>
                <div class="max-w-screen-xl flex flex-wrap items-baseline mx-auto p-4 mt-5">
                    <h5 class="mb-4 mr-4">Выдать диплом о высшем образовании</h5>
                    <div class="relative max-w-sm">
                        <select id="scoredip" v-model="selectedUser.scoredip" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" @change="ScoresPush(selectedUser)">
                            <option selected>Выберете оценку</option>
                            <option value="wotl">с отличием</option>
                            <option value="dotl">без отличия</option>
                        </select>
                    </div>
                </div>
            </div>  
        </div>
        <div class="w-full h-96 overflow-auto">
            <h1 class="text-center mb-3">Список студентов</h1>
            <ul class="text-center">
                <li class="text-center p-2 rounded-3xl bg-gray-300 mb-3" v-for="(user, index) in users" :key="index" @click="handleUserClick(index)">{{ index }}</li>
            </ul>
        </div>
    </div>
    <div class="flex items-center justify-center">
        <button class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-cyan-500 to-blue-500 group-hover:from-cyan-500 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-cyan-200 dark:focus:ring-cyan-800" @click="handleDownload">
            <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                Скачать файл
            </span>
        </button>
    </div>
</template>
  
<script>
  import axios from 'axios';
  import Nav from './Nav.vue';
  export default {
    name: 'Home',
    components:{
      Nav,
    },
    data() {
        return {
            namegospred: "",
            users: {},
            selectedUser: null,
        };
    },
    mounted() {
        this.loadstudent();
    },
    methods: {
        async handleFileUpload(event) {
            const fileInput = event.target;
            const file = fileInput.files[0];
            const formData = new FormData();
            formData.append('file', file);

            try {
            const response = await axios.post('http://127.0.0.1:83/upload', formData, {
                headers: {
                'Content-Type': 'multipart/form-data',
                },
            });
            if (response.data.status === "success") {
                await this.loadstudent();
            } else {
                console.error('Бэкенд вернул неуспешный ответ:', response.data);
            }
            } catch (error) {
            console.error('Ошибка при отправке файла:', error);
            }
        },
        async loadstudent() {
            try{
                const getresponse = await axios.get('http://127.0.0.1:83/getjsoninfo');
                this.users = getresponse.data.users;
            }
            catch(error){
                console.log(error)
            }
        },
        handleUserClick(index){
            this.selectedUser = this.users[index];
        },
        async ScoresPush(item){
            try{
                const postData = {
                    student: item.name,
                    score: item.score,
                    scoredip: item.scoredip,
                };
                const postresponse = await axios.post('http://127.0.0.1:83/getjsoninfo', postData);
                console.log(postresponse)
            }catch(error){
                console.log(error)
            }
        },
        handleDownload() {
            const data = {
                date: this.$refs.datepicker1.value,
                namegospred: this.namegospred,
                score: this.score,
                scoredip: this.scoredip
            };
            console.log(data)
        },
    },
};
</script>