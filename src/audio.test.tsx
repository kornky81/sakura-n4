import React from 'react';
import {afterEach,it,expect,vi} from 'vitest';
import {render,screen,fireEvent,cleanup} from '@testing-library/react';
import {Audio,browserSpeech} from './Audio';
afterEach(()=>{cleanup();vi.unstubAllGlobals();});
it('uses standard static audio even without a system voice',()=>{vi.stubGlobal('speechSynthesis',undefined);render(<Audio text="こんにちは。" src="/audio/fl2.mp3"/>);const player=screen.getByLabelText('Japanese listening recording');expect(player).toHaveAttribute('src','/audio/fl2.mp3');expect(player).toHaveAttribute('controls');expect(screen.queryByRole('alert')).toBeNull();});
it('reports recording errors and retries with a new player',()=>{render(<Audio text="こんにちは。"/>);const player=screen.getByLabelText('Japanese listening recording');fireEvent.error(player);expect(screen.getByRole('alert')).toHaveTextContent('could not be loaded');fireEvent.click(screen.getByRole('button',{name:'Retry recording'}));expect(screen.getByLabelText('Japanese listening recording')).not.toBe(player);});
it('handles missing Japanese voice gracefully',()=>{const onError=vi.fn();vi.stubGlobal('speechSynthesis',{getVoices:()=>[]});expect(browserSpeech('こんにちは',onError)).toBe(false);expect(onError).toHaveBeenCalledWith(expect.stringContaining('No Japanese system voice'));});
it('uses an available Japanese fallback voice only when requested',()=>{const speak=vi.fn();const voice={lang:'ja-JP'};vi.stubGlobal('speechSynthesis',{getVoices:()=>[voice],cancel:vi.fn(),speak});vi.stubGlobal('SpeechSynthesisUtterance',class{constructor(public text:string){} });render(<Audio text="こんにちは。"/>);expect(speak).not.toHaveBeenCalled();fireEvent.click(screen.getByRole('button',{name:'Optional browser voice'}));expect(speak).toHaveBeenCalledOnce();});
