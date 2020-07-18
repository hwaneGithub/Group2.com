/**
 * ==========================================
 * 변수 정의
 * ==========================================
 * */

// wrapper
const slideContainer = document.querySelector('.wrapper');

// slide container
const slide = document.querySelector('.slides');

// buttons
const nextBtn = document.getElementById('next-btn');
const prevBtn = document.getElementById('prev-btn');

// interval delay - 4초마다
const interval = 4000;

// slide 요소들을 모두 가져옴
let slides = document.querySelectorAll('.slide');

/**
 * index 초기값
 * first clone으로 0번째에 클론 요소가 붙기때문에 1부터 시작
 */
let index = 1;

// setInterval을 담기 위한 변수
let slideId;

/**
 * ==========================================
 * 0번째, 마지막번째 clone 요소 생성 및 삽입
 * ==========================================
 * */

 // 0번째 요소 clone
const firstClone = slides[0].cloneNode(true);

/**
 * 마지막 요소 clone
 * -1을 하는 이유는 0부터 카운팅 되기때문에
 * element.length의 길이대로 가져올 경우
 * 마지막에 빈 노드를 가져오게된다.
 */
const lastClone = slides[slides.length - 1].cloneNode(true);

// id 속성 적용
firstClone.id = 'first-clone'
lastClone.id = 'last-clone'

// 앞 뒤로 삽입
slide.append(firstClone);
slide.prepend(lastClone);


/**
 * index번째 node의 가로폭을 가져온다.
 * 전체적인 이동거리를 계산할때 필요한 수치.
 * 현재는 모두 동일한 사이즈이기때문에 index대신 0으로 적용해도 무방하다
 * */
const slideWidth = slides[index].clientWidth;

/** slide container에 translateX로 이동 할 거리를 초기값으로 넣어준다.
 * 맨 앞에 마지막 clone 요소가 있기 때문에
 * slide 1개분량만큼 좌측으로 이동시켜준다.
 */
slide.style.transform = `translateX(${-slideWidth * index}px)`

// 슬라이더를 실행시키는 함수
const startSlide = () => {

    // 앞에서 선언해준 slideId 변수에 setInterval을 담아 실행한다.
    slideId = setInterval(()=>{

        // next로 이동시키는 함수 실행
        moveToNextSlide();
    },interval); // delay 값
}


// slide 요소를 모두 가져오는 변수. 계속 사용되야하므로 getSlide에 담아둔다.
const getSlides = () => document.querySelectorAll('.slide');

/**
 * 기본적으로 이동은 transform과 transition을 이용해서 애니메이션을 시킨다.
 * transition이 정지될때마다 실행될 함수들이다.
 */
slide.addEventListener('transitionend', ()=>{

    // 모든 slide 요소를 가져온다
    slides = getSlides();

    /**
     * slide의 index번째 id가 첫번째 클론과 같다면
     * 즉, 마지막 요소에 도달했다면 실행.
     */
    if(slides[index].id === firstClone.id){
        /**
         * transition을 none으로 설정.
         * 부드럽게 애니메이션이 되지 않기때문에
         * 순간적으로 바꿔치기 되는 시각적 효과를 얻는다.
         * */
        slide.style.transition = 'none';

        // index값을 1로 - 첫번째 슬라이더로 위치시킨다
        index = 1;

        // 첫번째 슬라이더가 보이도록 위치값 설정
        slide.style.transform = `translateX(${-slideWidth * index}px)`;
    }

    /**
     * slide의 index번째 id가 마지막 클론과 같다면,
     * 즉, 첫번째 요소에 도달했다면 실행.
     */
    if(slides[index].id === lastClone.id){
        // 위의 if문과 같은 내용
        slide.style.transition = 'none';

        /**
         * 전체 노드 갯수(length)에서 -2를 하는 이유는
         * 0부터 세기때문에 맨 마지막 요소는 빈노드, -1번째는 클론 요소이기때문
         * */
        index = slides.length - 2;
        // 마지막 슬라이더로 위치시킨다.
        slide.style.transform = `translateX(${-slideWidth * index}px)`;
    }
});


/**
 * next slide로 이동시키는 함수
 */
const moveToNextSlide = () => {

    // 모든 노드를 가져옴
    slides = getSlides();

    // index 값이 마지막 노드보다 크거타 같으면 return으로 실행 skip
    if(index >= slides.length - 1) return;

    // index 값 증가
    index++;

    // 증가된 index 값을 곱한만큼 이동
    slide.style.transform = `translateX(${-slideWidth * index}px)`

    // transition 값 설정
    slide.style.transition = '.5s all ease-in-out';
}


/**
 * previous slide로 이동시키는 함수
 */
const moveToPreviousSlide = () => {

    // index값이 0보다 작거나 같으면 return으로 실행  skip
    if(index <= 0 ) return;

    // index 값 감소
    index--;

    // 감소된  index 값을 곱한만큼 이동
    slide.style.transform = `translateX(${-slideWidth * index}px)`

    // transition 값 설정
    slide.style.transition = '.5s all ease-in-out';

}


/**
 * 마우스가 슬라이더 위로 올라갔을 경우 슬라이더의 작동을 멈추는 함수
 */
slideContainer.addEventListener('mouseenter', ()=>{

    // clearInterval로 setInterval 중지
    clearInterval(slideId);
});


/**
 * 마우스가 슬라이더 위에서 사라지면 startSlide 함수 실행으로 슬라이더 작동
 */
slideContainer.addEventListener('mouseleave', startSlide);


/**
 * next 버튼을 누를 경우 moveToNextSlide로 슬라이더를
 * 다음 슬라이더로 한 번 이동
 */
nextBtn.addEventListener('click', moveToNextSlide);

/**
 * previous 버튼을 누를 경우 moveToPreviousSlide로
 * 슬라이더를 이전 슬라이더로 한 번 이동
 */
prevBtn.addEventListener('click', moveToPreviousSlide);


/**
 * 정해진 Delay 시간마다 슬라이더를 이동시키는 setInterval 실행
 */
startSlide();
