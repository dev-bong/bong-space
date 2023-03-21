<script>
    let menu_list = []

    function get_menu_list() {
        fetch("http://127.0.0.1:8000/api/category/list").then((response) => {
            response.json().then((json) => {
                menu_list = json
            })
        })
    }

    get_menu_list()
</script>

<div class="container my-3">
    <!-- 게시글 -->
    <h2 class="border-bottom py-2">메뉴 목록</h2>

    {#each menu_list as menu}
        <div class="card my-3">
            <div class="card-body">
                <div class="card-text" style="white-space: pre-line;">
                    <h5>{menu.name}</h5>
                    <p>
                        {menu.description}
                    </p>
                </div>
            </div>
        </div>
    {/each}
</div>