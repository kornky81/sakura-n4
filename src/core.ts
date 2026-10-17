import {kanji,questions} from './data';
export type Activity={id:string;subject:string;correct:boolean;at:string};
export type Attempt={id:string;examId?:string;at:string;answers:Record<string,number>;score:number;total:number};
export type State={examDate:string;minutes:number;romaji:boolean;statuses:Record<string,string>;due:Record<string,number>;activity:Activity[];attempts:Attempt[]};
export const initial:State={examDate:'',minutes:20,romaji:true,statuses:{},due:{},activity:[],attempts:[]};
export const dateKey=(d=new Date())=>`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
export function countdown(date:string,now=new Date()){if(!/^\d{4}-\d{2}-\d{2}$/.test(date))return null;const [y,m,d]=date.split('-').map(Number);return Math.max(0,Math.ceil((Date.UTC(y,m-1,d)-Date.UTC(now.getFullYear(),now.getMonth(),now.getDate()))/86400000));}
export const remaining=(deadline:number,now=Date.now())=>Math.max(0,Math.ceil((deadline-now)/1000));
export const score=(answers:Record<string,number>,ids=questions.map(q=>q.id))=>ids.reduce((n,id)=>n+Number(answers[id]===questions.find(q=>q.id===id)?.answer),0);
export function submit(answers:Record<string,number>,id:string):Attempt{return {id,at:new Date().toISOString(),answers:{...answers},score:score(answers),total:questions.length};}
export function load():State{try{const x=JSON.parse(localStorage.getItem('sakura-v1')||'null');if(!x||!Array.isArray(x.activity)||!Array.isArray(x.attempts)||typeof x.statuses!=='object')return {...initial};return {...initial,...x,minutes:Math.min(120,Math.max(5,Number(x.minutes)||20))};}catch{return {...initial};}}
export function persist(s:State){try{localStorage.setItem('sakura-v1',JSON.stringify(s));return true;}catch{return false;}}
export function streak(activity:Activity[]){const dates=new Set(activity.map(a=>dateKey(new Date(a.at))));const d=new Date();if(!dates.has(dateKey(d)))d.setDate(d.getDate()-1);let n=0;while(dates.has(dateKey(d))){n++;d.setDate(d.getDate()-1);}return n;}
export function audit(){return {cards:kanji.length,readings:kanji.flatMap(k=>k.readings).length,missing:kanji.flatMap(k=>k.readings).filter(r=>!r.word||!r.reading||!r.roman).length};}
