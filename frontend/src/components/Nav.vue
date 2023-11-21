<template>
    <nav class="bg-white border-gray-200 dark:bg-gray-900">
      <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <a href="/home" class="flex items-center space-x-3 rtl:space-x-reverse">
            <img src="../assets/logo.svg" class="pt-3 w-13 h-13" alt="Logo" />
        </a>
        <button data-collapse-toggle="navbar-default" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
            </svg>
        </button>
        <div class="hidden w-full md:block md:w-auto" id="navbar-default">
          <ul class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
            <li v-for="link in Links">
              <a :href="link.link" class="block py-2 px-3 text-white rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500" :class="{ 'bg-blue-700': isCurrentPage(link.link), 'text-white': isCurrentPage(link.link), 'dark:text-white': isCurrentPage(link.link) }" aria-current="page">{{ link.name }}</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>
  
<script>
  export default {
    name: 'Nav',
    setup(){
    let Links = [
      {name: "Заполнение документа", link: "/home"},
      {name: "Члены комиссии", link: "/members"},
      {name: "Черновики", link: "/drafts"},
    ]
    const isCurrentPage = (link) => {
      return window.location.pathname.endsWith(link);
    };

    return { Links, isCurrentPage };
  }
  };
</script>
  