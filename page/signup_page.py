signup_page_code = """
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NothingTime - Signup</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f7f7f7;
        }

        .signup-container {
            width: 400px;
            padding: 40px;
            background-color: #fff;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            border-radius: 10px;
        }

        .logo {
            margin-bottom: 20px;
        }

        .logo svg {
            width: 200px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group input {
            width: calc(100% - 20px);
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }

        .signup-button {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            background-color: #59B8FC;
            border: none;
            color: #fff;
            cursor: pointer;
            border-radius: 5px;
        }

        .signup-button:hover {
            background-color: #4aa7e0;
        }

        .additional-links {
            margin-top: 15px;
            font-size: 14px;
        }

        .additional-links a {
            color: #59B8FC;
            text-decoration: none;
        }

        .additional-links a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="signup-container">
        <div class="logo">
            <svg width="611" height="93" viewBox="0 0 611 93" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M7.07805e-08 73L12 7H33.5L49.1 52.4L57.4 7L68.5 7.1L56.3 73H33.4L19 29.3L11 73H7.07805e-08ZM92.8125 75C78.1458 75 70.8125 68.1 70.8125 54.3C70.8125 44.5 73.5125 36.4333 78.9125 30.1C84.6458 23.3667 92.4792 20 102.413 20C109.613 20 115.046 21.6667 118.713 25C122.379 28.3333 124.213 33.5 124.213 40.5C124.213 51.1667 121.346 59.6 115.613 65.8C110.013 71.9333 102.413 75 92.8125 75ZM95.4125 31.5C94.6125 33.3 93.8792 35.5667 93.2125 38.3C92.6125 40.9667 91.9125 44.4333 91.1125 48.7C90.3125 52.9667 89.9125 57.7333 89.9125 63C89.9125 64.7333 90.1792 66.1667 90.7125 67.3C91.3125 68.4333 92.3792 69 93.9125 69C95.4458 69 96.6792 68.6333 97.6125 67.9C98.6125 67.1667 99.4792 65.9333 100.213 64.2C101.546 61.1333 102.746 56.7667 103.813 51.1C104.879 45.3667 105.446 41.2667 105.513 38.8C105.646 36.3333 105.713 34.2 105.713 32.4C105.713 30.5333 105.446 29 104.913 27.8C104.379 26.6 103.346 26 101.813 26C100.346 26 99.1125 26.4667 98.1125 27.4C97.1125 28.3333 96.2125 29.7 95.4125 31.5ZM131.695 63C131.695 61.2 132.161 58.0333 133.095 53.5L138.395 26.5H132.495L132.895 23.5C140.895 21.1 148.761 16.9667 156.495 11.1H161.295L158.895 22H166.695L165.795 26.5H158.095L152.995 53.5C152.128 57.6333 151.695 60.4 151.695 61.8C151.695 65 153.095 66.9333 155.895 67.6C155.228 69.8667 153.695 71.6667 151.295 73C148.895 74.3333 145.995 75 142.595 75C139.195 75 136.528 73.9333 134.595 71.8C132.661 69.6667 131.695 66.7333 131.695 63ZM216.527 61.9C216.527 64.8333 218.027 66.7333 221.027 67.6C220.294 70.0667 218.494 71.9667 215.627 73.3C213.227 74.4333 210.694 75 208.027 75C205.427 75 203.427 74.6333 202.027 73.9C200.694 73.2333 199.661 72.3333 198.927 71.2C197.727 69.4667 197.127 66.9667 197.127 63.7C197.127 61.7667 197.661 58.1333 198.727 52.8L200.127 45.2C201.261 39.4 201.827 35.4333 201.827 33.3C201.827 29.5667 200.794 27.7 198.727 27.7C196.127 27.7 193.994 29.6 192.327 33.4C191.661 34.8667 191.094 36.7 190.627 38.9L183.827 73L163.727 75L177.827 3L197.927 0.999997L197.127 5C195.261 15.2667 193.527 22.1333 191.927 25.6C195.661 21.8667 200.961 20 207.827 20C215.094 20 219.394 22.4 220.727 27.2C221.194 28.7333 221.427 30.1667 221.427 31.5C221.427 32.8333 221.361 34.0333 221.227 35.1C221.161 36.1 220.961 37.5333 220.627 39.4L219.327 46.6L217.027 57.9C216.694 59.4333 216.527 60.7667 216.527 61.9ZM253.118 67.5C251.051 72.5 246.718 75 240.118 75C236.718 75 233.951 73.8333 231.818 71.5C230.018 69.4333 229.118 67.3667 229.118 65.3C229.118 59.9 230.351 51.9333 232.818 41.4L236.518 22L256.818 20L250.718 51.6C249.585 56.5333 249.018 59.8667 249.018 61.6C249.018 65.4 250.385 67.3667 253.118 67.5ZM238.318 8.1C238.318 5.5 239.385 3.5 241.518 2.09999C243.718 0.699997 246.385 -1.90735e-06 249.518 -1.90735e-06C252.651 -1.90735e-06 255.151 0.699997 257.018 2.09999C258.951 3.5 259.918 5.5 259.918 8.1C259.918 10.7 258.851 12.6667 256.718 14C254.651 15.3333 252.051 16 248.918 16C245.785 16 243.218 15.3333 241.218 14C239.285 12.6667 238.318 10.7 238.318 8.1ZM303.938 75C295.871 75 291.838 71.8667 291.838 65.6C291.904 63.8667 292.204 61.5333 292.738 58.6L294.538 49.4C296.338 40.7333 297.238 35.4333 297.238 33.5C297.238 29.6333 296.104 27.7 293.838 27.7C290.038 27.7 287.138 32.6667 285.138 42.6L279.238 73L259.137 75L269.538 21.9L285.938 20L284.338 29.8C287.471 23.2667 293.838 20 303.438 20C308.104 20 311.404 21 313.338 23C315.338 24.9333 316.338 28.1 316.338 32.5C316.338 36.6333 315.271 43.5333 313.138 53.2C312.138 57.5333 311.638 60.5333 311.638 62.2C311.638 63.8 312.071 65.0667 312.938 66C313.871 66.9333 315.004 67.4667 316.338 67.6C315.671 69.8667 314.171 71.6667 311.838 73C309.571 74.3333 306.938 75 303.938 75ZM331.433 31.2C333.699 28 336.533 25.3333 339.933 23.2C343.399 21.0667 347.233 20 351.433 20C355.633 20 358.733 20.6667 360.733 22L380.333 20L373.533 58.4C371.199 71.4667 367.566 80.5667 362.633 85.7C357.899 90.5667 350.933 93 341.733 93C334.733 93 329.233 91.9 325.233 89.7C321.233 87.5 319.233 84.5667 319.233 80.9C319.233 78.1667 320.266 76 322.333 74.4C324.399 72.8667 327.033 72.1 330.233 72.1C333.033 72.1 335.499 72.7333 337.633 74C338.899 74.6667 339.833 75.4667 340.433 76.4C338.899 77.7333 338.133 79.5 338.133 81.7C338.133 84.5667 339.466 86 342.133 86C346.599 86 350.099 80.7333 352.633 70.2C353.366 67.3333 354.033 64.4667 354.633 61.6C351.633 65.2667 346.733 67.1 339.933 67.1C335.199 67.1 331.466 65.9667 328.733 63.7C325.999 61.4333 324.633 57.6333 324.633 52.3C324.633 48.9667 325.199 45.4333 326.333 41.7C327.466 37.9 329.166 34.4 331.433 31.2ZM344.433 52.6C344.433 57.1333 345.599 59.4 347.933 59.4C349.533 59.4 351.099 58.5333 352.633 56.8C353.833 55.4 354.666 53.6667 355.133 51.6L360.233 25.9C359.899 25.8333 359.566 25.7333 359.233 25.6C358.566 25.3333 357.799 25.2 356.933 25.2C352.866 25.2 349.633 28.5333 347.233 35.2C345.366 40.4 344.433 46.2 344.433 52.6ZM392.196 24.3C389.929 22.5667 388.796 19.8667 388.796 16.2C388.796 12.4667 389.996 9.63333 392.396 7.69999C394.863 5.76666 398.196 4.8 402.396 4.8C405.063 4.8 409.563 5.26666 415.896 6.2L422.696 7.19999C424.963 7.46666 427.263 7.6 429.596 7.6C431.996 7.6 433.996 7.1 435.596 6.1C437.996 8.23333 439.196 10.8333 439.196 13.9C439.196 16.9667 437.829 19.6 435.096 21.8C432.296 24.1333 429.096 25.3 425.496 25.3C423.763 25.3 421.496 25.0667 418.696 24.6C415.429 34.8667 413.796 43.5667 413.796 50.7C413.796 57.8333 415.596 63.2667 419.196 67C417.529 70 415.463 72.0667 412.996 73.2C410.529 74.4 407.429 75 403.696 75C400.029 75 397.029 74 394.696 72C392.429 69.9333 391.296 66.8 391.296 62.6C391.296 57.7333 392.629 51.3 395.296 43.3C397.963 35.3667 401.296 28.3667 405.296 22.3C403.363 22.1 401.396 22 399.396 22C395.263 22 392.863 22.7667 392.196 24.3ZM459.954 67.5C457.887 72.5 453.554 75 446.954 75C443.554 75 440.787 73.8333 438.654 71.5C436.854 69.4333 435.954 67.3667 435.954 65.3C435.954 59.9 437.187 51.9333 439.654 41.4L443.354 22L463.654 20L457.554 51.6C456.421 56.5333 455.854 59.8667 455.854 61.6C455.854 65.4 457.221 67.3667 459.954 67.5ZM445.154 8.1C445.154 5.5 446.221 3.5 448.354 2.09999C450.554 0.699997 453.221 -1.90735e-06 456.354 -1.90735e-06C459.487 -1.90735e-06 461.987 0.699997 463.854 2.09999C465.787 3.5 466.754 5.5 466.754 8.1C466.754 10.7 465.687 12.6667 463.554 14C461.487 15.3333 458.887 16 455.754 16C452.621 16 450.054 15.3333 448.054 14C446.121 12.6667 445.154 10.7 445.154 8.1ZM540.473 75C532.407 75 528.373 71.8667 528.373 65.6C528.373 62.8667 528.94 58.8667 530.073 53.6C531.273 48.2667 532.073 44.5333 532.473 42.4C533.407 37.5333 533.873 34.3333 533.873 32.8C533.873 29.4 532.607 27.7 530.073 27.7C528.407 27.7 526.773 28.8667 525.173 31.2C523.573 33.4667 522.407 36.9 521.673 41.5L515.473 73L495.973 75L501.373 47.8C501.973 44.8 502.54 41.6 503.073 38.2C503.607 34.8 503.873 32.8333 503.873 32.3C503.873 29.2333 502.74 27.7 500.473 27.7C498.94 27.7 497.34 28.8333 495.673 31.1C494.007 33.3667 492.707 36.8333 491.773 41.5L485.673 73L465.973 75L476.473 22L492.773 20L491.073 30.1C492.807 26.5 495.273 23.9333 498.473 22.4C501.673 20.8 505.773 20 510.773 20C513.64 20 516.007 20.7 517.873 22.1C519.74 23.5 520.973 25.3333 521.573 27.6C522.707 25.2667 524.707 23.4333 527.573 22.1C530.507 20.7 533.74 20 537.273 20C540.873 20 543.54 20.4 545.273 21.2C547.073 21.9333 548.507 22.9333 549.573 24.2C551.373 26.5333 552.273 29.8333 552.273 34.1C552.273 38.3 551.373 44.7667 549.573 53.5C548.64 57.7667 548.173 60.7 548.173 62.3C548.173 63.8333 548.607 65.0667 549.473 66C550.407 66.9333 551.54 67.4667 552.873 67.6C552.207 69.8667 550.707 71.6667 548.373 73C546.107 74.3333 543.473 75 540.473 75ZM601.063 56.1C602.73 57.2333 603.563 59.0667 603.563 61.6C603.563 64.0667 602.93 66.1 601.663 67.7C600.397 69.3 598.73 70.6333 596.663 71.7C592.397 73.9 587.963 75 583.363 75C578.763 75 575.097 74.5 572.363 73.5C569.697 72.5 567.463 71.0667 565.663 69.2C562.13 65.6667 560.363 60.6667 560.363 54.2C560.363 44.1333 563.097 36.0333 568.563 29.9C574.43 23.3 582.463 20 592.663 20C598.997 20 603.73 21.3333 606.863 24C609.197 26 610.363 28.6333 610.363 31.9C610.363 43.6333 600.23 49.5 579.963 49.5C579.697 51.2333 579.563 52.8333 579.563 54.3C579.563 57.3667 580.23 59.5 581.563 60.7C582.963 61.8333 584.93 62.4 587.463 62.4C589.997 62.4 592.597 61.8333 595.263 60.7C597.997 59.5 599.93 57.9667 601.063 56.1ZM580.663 45.2C585.397 45.2 589.13 43.7333 591.863 40.8C594.597 38 595.963 34.3667 595.963 29.9C595.963 28.3667 595.663 27.2 595.063 26.4C594.53 25.5333 593.697 25.1 592.563 25.1C591.43 25.1 590.363 25.3333 589.363 25.8C588.43 26.2 587.463 27.1333 586.463 28.6C583.997 31.9333 582.063 37.4667 580.663 45.2Z"
                    fill="#59B8FC" />
            </svg>
        </div>
        <form method="POST" action="https://port-0-nothingtime-lzsaeexf05f2c47e.sel4.cloudtype.app/signup">
            <div class="form-group">
                <input type="text" placeholder="ID" required>
            </div>
            <div class="form-group">
                <input type="password" placeholder="Password" required>
            </div>
            <div class="form-group">
                <input type="password" placeholder="Confirm Password" required>
            </div>
            <button type="submit" class="signup-button">회원가입</button>
        </form>
        <div class="additional-links">
            <a href="https://port-0-nothingtime-lzsaeexf05f2c47e.sel4.cloudtype.app/login">이미 NothingTime 계정이 있으신가요? 로그인
                하기</a>
        </div>
    </div>
</body>

</html>
"""