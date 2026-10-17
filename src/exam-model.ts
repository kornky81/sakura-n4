import {questions,sections,type Question} from './data';
import written from './mock-written.json';
import listening from './mock-listening.json';
import {type Attempt} from './core';
export type ExamSection={name:string;seconds:number;ids:string[]};
export type ExamDefinition={id:string;title:string;description:string;sections:ExamSection[];questions:Question[];fullLength:boolean};
export const fullQuestions:Question[]=[...written,...listening];
export const shortExam:ExamDefinition={id:'SAKURA-SAMPLE-01',title:'Short Practice Exam',description:'10 questions · 11 minutes 30 seconds · a shortened practice test',sections,questions,fullLength:false};
export const fullExam:ExamDefinition={id:'SAKURA-FULL-01',title:'Full Mock Exam 01',description:'85 original questions · 115 minutes · full-length validation draft',fullLength:true,questions:fullQuestions,sections:[{name:'Vocabulary',seconds:25*60,ids:fullQuestions.filter(q=>q.subject==='Vocabulary').map(q=>q.id)},{name:'Grammar & reading',seconds:55*60,ids:fullQuestions.filter(q=>q.subject==='Grammar'||q.subject==='Reading').map(q=>q.id)},{name:'Listening',seconds:35*60,ids:fullQuestions.filter(q=>q.subject==='Listening').map(q=>q.id)}]};
export const exams=[shortExam,fullExam];
export const getExam=(id?:string)=>exams.find(e=>e.id===id)||shortExam;
export type ExamSession={id:string;examId:string;section:number;deadline:number;answers:Record<string,number>};
export function startExam(exam:ExamDefinition,now=Date.now(),id:string=crypto.randomUUID()):ExamSession{return {id,examId:exam.id,section:0,deadline:now+exam.sections[0].seconds*1000,answers:{}};}
export function readSession(storage:Pick<Storage,'getItem'>=localStorage):ExamSession|null{try{const raw=JSON.parse(storage.getItem('sakura-exam')||'null');if(!raw||typeof raw.id!=='string'||!Number.isFinite(raw.deadline)||!Number.isInteger(raw.section)||raw.section<0||raw.section>2||!raw.answers||typeof raw.answers!=='object'||(raw.examId&&!exams.some(e=>e.id===raw.examId)))return null;const exam=getExam(raw.examId);const answers:Record<string,number>={};for(const q of exam.questions){const a=raw.answers[q.id];if(Number.isInteger(a)&&a>=0&&a<q.options.length)answers[q.id]=a;}return {...raw,examId:exam.id,answers};}catch{return null;}}
export function saveSession(s:ExamSession|null,storage:Pick<Storage,'setItem'|'removeItem'>=localStorage){try{if(s)storage.setItem('sakura-exam',JSON.stringify(s));else storage.removeItem('sakura-exam');return true;}catch{return false;}}
export function selectAnswer(s:ExamSession,id:string,answer:number,now=Date.now()):ExamSession{const exam=getExam(s.examId);const q=exam.questions.find(q=>q.id===id);if(now>=s.deadline||!exam.sections[s.section].ids.includes(id)||!q||!Number.isInteger(answer)||answer<0||answer>=q.options.length)return s;return {...s,answers:{...s.answers,[id]:answer}};}
export function nextSection(s:ExamSession,now=Date.now()):ExamSession|null{const exam=getExam(s.examId);if(s.section===exam.sections.length-1)return null;return {...s,section:s.section+1,deadline:now+exam.sections[s.section+1].seconds*1000};}
// Expired sections use their original boundary, not the refresh time. A long absence
// cannot grant extra exam time. A manually finished section starts the next at now.
export function recoverExpired(s:ExamSession,now=Date.now()):{session:ExamSession;finished:boolean}{let current=s;while(now>=current.deadline){const next=nextSection(current,current.deadline);if(!next)return {session:current,finished:true};current=next;}return {session:current,finished:false};}
export function gradeExam(s:ExamSession):Attempt{const exam=getExam(s.examId);return {id:s.id,examId:exam.id,at:new Date().toISOString(),answers:{...s.answers},score:exam.questions.filter(q=>s.answers[q.id]===q.answer).length,total:exam.questions.length};}
export function sectionScore(exam:ExamDefinition,section:ExamSection,answers:Record<string,number>){return section.ids.filter(id=>answers[id]===exam.questions.find(q=>q.id===id)?.answer).length;}
export const listeningItems=listening as Question[];
