require_relative './string_compression_solution_2.rb'
RSpec.describe 'string compression' do
    subject { StringPress.new }
    describe 'when string compresses' do
        context 'with more than three characters' do
            it 'compresses the string' do
                expect(subject.compress('aabcccccaaa')).to eq('a2b1c5a3')
                expect(subject.compress_word('aabcccccaaa')).to eq('a2b1c5a3')
            end
        end
    end
    describe "when string doesnt compress" do
        context "with less than three characters" do
            it 'different characters returns the same string' do
                expect(subject.compress('ab')).to eq('ab')
                expect(subject.compress_word('ba')).to eq('ba')
            end
            it 'same characters returns the same string' do
                expect(subject.compress('bb')).to eq('bb')
                expect(subject.compress_word('aa')).to eq('aa')
            end
        end

        context "with more than three characters" do
            it 'returns string when characters dont compress' do
                expect(subject.compress('abc')).to eq('abc')
                expect(subject.compress_word('bac')).to eq('bac')
            end
        end
    end
end